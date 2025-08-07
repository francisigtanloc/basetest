# Checkpoint 1
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from baserow.contrib.database.models import Database
from baserow.contrib.database.table.models import Table
from baserow.contrib.database.fields.models import Field
from baserow.api.decorators import map_exceptions, validate_body
from rest_framework.exceptions import AuthenticationFailed
# Checkpoint 1 - END

# Checkpoint 2
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .schemas import (
    authenticate_user_schema,
    create_user_response_schema,
    verify_user_schema,
)
from baserow.api.schemas import get_error_schema

from .serializers import (
    AccountSerializer,
    ChangePasswordBodyValidationSerializer,
    DashboardSerializer,
    LmsTokenObtainPairSerializer,
    NormalizedEmailField,
    PublicUserSerializer,
    RegisterSerializer,
    ResetPasswordBodyValidationSerializer,
    SendResetPasswordEmailBodyValidationSerializer,
    SendVerifyEmailAddressSerializer,
    ShareOnboardingDetailsWithBaserowSerializer,
    TokenBlacklistSerializer,
    TokenObtainPairWithUserSerializer,
    TokenRefreshWithUserSerializer,
    TokenVerifyWithUserSerializer,
    UserSerializer,
    VerifyEmailAddressSerializer,
)
from baserow.core.auth_provider.exceptions import (
    AuthProviderDisabled,
    EmailVerificationRequired,
)
from baserow.core.auth_provider.handler import PasswordProviderHandler
from baserow.core.exceptions import (
    BaseURLHostnameNotAllowed,
    LockConflict,
    WorkspaceInvitationDoesNotExist,
    WorkspaceInvitationEmailMismatch,
)
from baserow.core.handler import CoreHandler
from baserow.core.models import Settings, Template, WorkspaceInvitation
from baserow.core.user.actions import (
    ChangeUserPasswordActionType,
    CreateUserActionType,
    ResetUserPasswordActionType,
    ScheduleUserDeletionActionType,
    SendResetUserPasswordActionType,
    SendVerifyEmailAddressActionType,
    UpdateUserActionType,
    VerifyEmailAddressActionType,
)
from baserow.core.user.exceptions import (
    DeactivatedUserException,
    DisabledSignupError,
    EmailAlreadyVerified,
    InvalidPassword,
    InvalidVerificationToken,
    RefreshTokenAlreadyBlacklisted,
    ResetPasswordDisabledError,
    UserAlreadyExist,
    UserIsLastAdmin,
    UserNotFound,
)
from .errors import (
    ERROR_ALREADY_EXISTS,
    ERROR_AUTH_PROVIDER_DISABLED,
    ERROR_CLIENT_SESSION_ID_HEADER_NOT_SET,
    ERROR_DEACTIVATED_USER,
    ERROR_DISABLED_RESET_PASSWORD,
    ERROR_DISABLED_SIGNUP,
    ERROR_EMAIL_ALREADY_VERIFIED,
    ERROR_EMAIL_VERIFICATION_REQUIRED,
    ERROR_INVALID_CREDENTIALS,
    ERROR_INVALID_OLD_PASSWORD,
    ERROR_INVALID_REFRESH_TOKEN,
    ERROR_INVALID_VERIFICATION_TOKEN,
    ERROR_REFRESH_TOKEN_ALREADY_BLACKLISTED,
    ERROR_UNDO_REDO_LOCK_CONFLICT,
    ERROR_USER_IS_LAST_ADMIN,
    ERROR_USER_NOT_FOUND,
)


# Checkpoint 2 - END


# Checkpoint 1 Classes
class StartingView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({"title": "Starting title", "content": "Starting text"})

class CoursesView(APIView):
    permission_classes = (AllowAny,)
    
    def get_model_and_table(self):
        """Helper method to get the model and table"""
        database = Database.objects.get(name="Hublms")
        table = Table.objects.get(database=database, name="Courses")
        model = table.get_model()
        return model, table
    
    def get_course_data(self, course):
        """Helper method to format course data"""
        import logging
        logger = logging.getLogger(__name__)
        
        try:
            # Get all field objects from the model
            field_objects = course.get_field_objects()
            
            # Prepare the course data with actual field values
            course_data = {
                'id': course.id,
                'order': str(course.order)  # Convert Decimal to string for JSON serialization
            }
            
            # Add all custom fields from the table
            for field_object in field_objects:
                field_name = field_object['field'].name
                field_type = field_object['type'].type
                
                try:
                    field_value = getattr(course, f'field_{field_object["field"].id}')
                    
                    # Convert field value based on its type
                    if field_value is not None:
                        if field_type == 'number':
                            field_value = float(field_value) if field_value is not None else None
                        elif field_type == 'boolean':
                            field_value = bool(field_value)
                        elif field_type in ['date', 'last_modified', 'created_on']:
                            field_value = field_value.isoformat() if field_value else None
                    
                    course_data[field_name] = field_value
                except Exception as e:
                    logger.warning(f"Could not get field {field_name}: {str(e)}")
                    course_data[field_name] = None
            
            # Add timestamps
            course_data.update({
                'created_on': course.created_on.isoformat() if course.created_on else None,
                'updated_on': course.updated_on.isoformat() if course.updated_on else None
            })
            
            return course_data
            
        except Exception as e:
            logger.error(f"Error getting course data: {str(e)}")
            raise

    def get(self, request, course_id=None):
        """
        GET /api/basetest/courses/ - List all courses
        GET /api/basetest/courses/{id}/ - Get single course
        """
        try:
            model, _ = self.get_model_and_table()
            
            # Get single course
            if course_id:
                course = model.objects.get(id=course_id)
                return Response({
                    "status": "success",
                    "course": self.get_course_data(course)
                })
            
            # Get all courses
            courses = model.objects.all()
            courses_data = [self.get_course_data(course) for course in courses]
            
            return Response({
                "status": "success",
                "count": len(courses_data),
                "courses": courses_data
            })
            
        except model.DoesNotExist:
            return Response({"error": "Course not found"}, status=404)
        except Database.DoesNotExist:
            return Response({"error": "Database 'Hublms' not found"}, status=404)
        except Table.DoesNotExist:
            return Response({"error": "Table 'Courses' not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        """
        POST /api/basetest/courses/ - Create a new course
        """
        try:
            model, table = self.get_model_and_table()
            data = request.data
            
            # Get field mappings
            field_objects = {}
            for field_obj in model.get_field_objects():
                field_name = field_obj['field'].name
                field_objects[field_name] = field_obj
            
            # Prepare course data with field mappings
            course_data = {}
            for field_name, value in data.items():
                if field_name in field_objects:
                    field_obj = field_objects[field_name]
                    field_id = field_obj['field'].id
                    field_type = field_obj['type'].type
                    
                    # Convert value based on field type
                    if value is not None:
                        if field_type == 'number':
                            value = float(value) if value != '' else None
                        elif field_type == 'boolean':
                            value = bool(value)
                    
                    course_data[f'field_{field_id}'] = value
            
            # Create the course
            course = model.objects.create(**course_data)
            
            return Response({
                "status": "success",
                "message": "Course created successfully",
                "course": self.get_course_data(course)
            }, status=201)
            
        except Exception as e:
            import traceback
            logger.error(f"Error creating course: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)
    
    def put(self, request, course_id):
        """
        PUT /api/basetest/courses/{id}/ - Update a course
        """
        try:
            model, table = self.get_model_and_table()
            
            # Get the course to update
            course = model.objects.get(id=course_id)
            data = request.data
            
            # Get field mappings
            field_objects = {}
            for field_obj in model.get_field_objects():
                field_name = field_obj['field'].name
                field_objects[field_name] = field_obj
            
            # Update fields
            for field_name, value in data.items():
                if field_name in field_objects:
                    field_obj = field_objects[field_name]
                    field_id = field_obj['field'].id
                    field_type = field_obj['type'].type
                    
                    # Convert value based on field type
                    if value is not None:
                        if field_type == 'number':
                            value = float(value) if value != '' else None
                        elif field_type == 'boolean':
                            value = bool(value)
                    
                    setattr(course, f'field_{field_id}', value)
            
            # Save changes
            course.save()
            
            return Response({
                "status": "success",
                "message": "Course updated successfully",
                "course": self.get_course_data(course)
            })
            
        except model.DoesNotExist:
            return Response({"error": "Course not found"}, status=404)
        except Exception as e:
            import traceback
            logger.error(f"Error updating course: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)

# Debug view for authentication testing
class DebugAuthView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request):
        """Debug endpoint to check available databases and tables, and show Users table data"""
        try:
            # Get all databases
            databases = Database.objects.all()
            db_info = []
            users_data = None
            
            for db in databases:
                tables = Table.objects.filter(database=db)
                table_info = []
                
                for table in tables:
                    # Get fields for each table
                    fields = Field.objects.filter(table=table)
                    field_info = [{"name": field.name, "type": field.__class__.__name__} for field in fields]
                    table_info.append({
                        "name": table.name,
                        "id": table.id,
                        "fields": field_info
                    })
                    
                    # If this is the Users table, get the actual data
                    if table.name == "Users":
                        try:
                            model = table.get_model()
                            users = model.objects.all()
                            users_list = []
                            
                            # Get field mappings
                            field_mappings = {}
                            for field_obj in model.get_field_objects():
                                field_name = field_obj['field'].name.lower()
                                field_id = field_obj['field'].id
                                field_mappings[field_name] = field_id
                            
                            for user in users[:5]:  # Limit to first 5 users
                                user_data = {"id": user.id}
                                for field_name, field_id in field_mappings.items():
                                    try:
                                        value = getattr(user, f'field_{field_id}', None)
                                        user_data[field_name] = value
                                    except:
                                        user_data[field_name] = None
                                users_list.append(user_data)
                            
                            users_data = {
                                "field_mappings": field_mappings,
                                "users": users_list,
                                "total_count": users.count()
                            }
                        except Exception as e:
                            users_data = {"error": str(e)}
                
                db_info.append({
                    "name": db.name,
                    "id": db.id,
                    "tables": table_info
                })
            
            response_data = {
                "databases": db_info
            }
            
            if users_data:
                response_data["users_table_data"] = users_data
            
            return Response(response_data)
            
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        """Test authentication with provided credentials, or add test user"""
        try:
            action = request.data.get('action', 'test_auth')
            
            if action == 'add_test_user':
                # Add a test user to the Users table
                database = Database.objects.get(name="Hublms")
                table = Table.objects.get(database=database, name="Users")
                model = table.get_model()
                
                # Get field mappings
                field_mappings = {}
                for field_obj in model.get_field_objects():
                    field_name = field_obj['field'].name.lower()
                    field_id = field_obj['field'].id
                    field_mappings[field_name] = field_id
                
                # Create test user data
                test_user_data = {}
                if 'name' in field_mappings:
                    test_user_data[f'field_{field_mappings["name"]}'] = 'Test User'
                if 'email' in field_mappings:
                    test_user_data[f'field_{field_mappings["email"]}'] = 'test@email.com'
                if 'active' in field_mappings:
                    test_user_data[f'field_{field_mappings["active"]}'] = True
                if 'password' in field_mappings:
                    test_user_data[f'field_{field_mappings["password"]}'] = 'testpassword123'
                
                # Check if user already exists
                existing_user = model.objects.filter(**{f'field_{field_mappings["email"]}': 'test@email.com'}).first()
                if existing_user:
                    return Response({
                        "success": True,
                        "message": "Test user already exists",
                        "user_id": existing_user.id
                    })
                
                # Create the test user
                user = model.objects.create(**test_user_data)
                
                return Response({
                    "success": True,
                    "message": "Test user created successfully",
                    "user_id": user.id,
                    "field_mappings": field_mappings
                })
            
            else:  # Default test_auth action
                from basetest.authentication import BaserowUserBackend
                
                email = request.data.get('email')
                password = request.data.get('password')
                
                if not email or not password:
                    return Response({"error": "Email and password required"}, status=400)
                
                backend = BaserowUserBackend()
                
                # Test authentication
                user = backend.authenticate(request, username=email, password=password)
                
                if user:
                    return Response({
                        "success": True,
                        "user": {
                            "id": user.id,
                            "email": getattr(user, 'email', 'N/A'),
                            "name": getattr(user, 'first_name', 'N/A'),
                            "is_active": getattr(user, 'is_active', 'N/A')
                        }
                    })
                else:
                    return Response({
                        "success": False,
                        "message": "Authentication failed"
                    })
                
        except Exception as e:
            import traceback
            return Response({
                "error": str(e),
                "traceback": traceback.format_exc()
            }, status=500)

# Checkpoint 1 Classes - END

class ObtainJSONWebTokens(TokenObtainPairView):
    """
    A slightly modified version of the ObtainJSONWebToken that uses an email as
    username and normalizes that email address using the normalize_email_address
    utility function. Now authenticates against the lms_users table.
    """

    serializer_class = LmsTokenObtainPairSerializer

    @extend_schema(
        tags=["User"],
        operation_id="token_auth",
        description=(
            "Authenticates an existing user based on their email and their password. "
            "If successful, an access token and a refresh token will be returned."
        ),
        responses={
            200: create_user_response_schema,
            401: get_error_schema(
                [
                    "ERROR_INVALID_CREDENTIALS",
                    "ERROR_DEACTIVATED_USER",
                    "ERROR_AUTH_PROVIDER_DISABLED",
                    "ERROR_EMAIL_VERIFICATION_REQUIRED",
                ]
            ),
        },
        auth=[],
    )
    @map_exceptions                                                                                                                                                                                                                   (
        {
            AuthenticationFailed: ERROR_INVALID_CREDENTIALS,
            DeactivatedUserException: ERROR_DEACTIVATED_USER,
            AuthProviderDisabled: ERROR_AUTH_PROVIDER_DISABLED,
            EmailVerificationRequired: ERROR_EMAIL_VERIFICATION_REQUIRED,
        }
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)



