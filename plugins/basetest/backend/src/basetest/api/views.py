import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed
from drf_spectacular.utils import extend_schema

from baserow.contrib.database.models import Database
from baserow.contrib.database.table.models import Table
from baserow.contrib.database.fields.models import Field
from baserow.api.decorators import map_exceptions
from baserow.api.schemas import get_error_schema
from baserow.core.auth_provider.exceptions import (
    AuthProviderDisabled,
    EmailVerificationRequired,
)
from baserow.core.user.exceptions import DeactivatedUserException

from .serializers import LmsTokenObtainPairSerializer
from .schemas import create_user_response_schema
from .errors import (
    ERROR_INVALID_CREDENTIALS,
    ERROR_DEACTIVATED_USER,
    ERROR_AUTH_PROVIDER_DISABLED,
    ERROR_EMAIL_VERIFICATION_REQUIRED,
)

logger = logging.getLogger(__name__)


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
                        elif field_type in ['created_by', 'last_modified_by'] or str(type(field_value).__name__) == 'User':
                            # Handle User objects
                            if hasattr(field_value, 'email'):
                                field_value = {
                                    'id': field_value.id,
                                    'email': field_value.email,
                                    'first_name': getattr(field_value, 'first_name', ''),
                                    'last_name': getattr(field_value, 'last_name', '')
                                }
                            else:
                                field_value = {'id': field_value.id, 'value': str(field_value)}
                        elif field_type == 'link_row':
                            # Handle Baserow link table relationships
                            if field_value:
                                if hasattr(field_value, 'all'):
                                    # Many-to-many relationship - get all related objects
                                    related_items = []
                                    for related_obj in field_value.all():
                                        # Try to get a meaningful display value
                                        display_value = str(related_obj.id)
                                        # Look for common display fields
                                        for attr in ['name', 'title', 'display_name', 'value']:
                                            if hasattr(related_obj, f'field_{attr}'):
                                                try:
                                                    attr_value = getattr(related_obj, f'field_{attr}')
                                                    if attr_value:
                                                        display_value = str(attr_value)
                                                        break
                                                except:
                                                    continue
                                        related_items.append({'id': related_obj.id, 'value': display_value})
                                    field_value = related_items
                                elif hasattr(field_value, 'id'):
                                    # Single relationship
                                    display_value = str(field_value.id)
                                    # Look for common display fields
                                    for attr in ['name', 'title', 'display_name', 'value']:
                                        if hasattr(field_value, f'field_{attr}'):
                                            try:
                                                attr_value = getattr(field_value, f'field_{attr}')
                                                if attr_value:
                                                    display_value = str(attr_value)
                                                    break
                                            except:
                                                continue
                                    field_value = {'id': field_value.id, 'value': display_value}
                                else:
                                    field_value = None
                    
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
            logger.error(f"Error creating course: {str(e)}\\n{traceback.format_exc()}")
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
            logger.error(f"Error updating course: {str(e)}\\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)
    
    def delete(self, request, course_id):
        """
        DELETE /api/basetest/courses/{id}/ - Delete a course
        """
        try:
            model, table = self.get_model_and_table()
            
            # Get the course to delete
            course = model.objects.get(id=course_id)
            course_data = self.get_course_data(course)  # Get data before deletion
            
            # Delete the course
            course.delete()
            
            return Response({
                "status": "success",
                "message": "Course deleted successfully",
                "deleted_course": course_data
            })
            
        except model.DoesNotExist:
            return Response({"error": "Course not found"}, status=404)
        except Exception as e:
            import traceback
            logger.error(f"Error deleting course: {str(e)}\\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)


class SampleView(APIView):
    permission_classes = (AllowAny,)
    
    def get_model_and_table(self):
        """Helper method to get the model and table"""
        database = Database.objects.get(name="Hublms")
        table = Table.objects.get(database=database, name="Sampler")
        model = table.get_model()
        return model, table
    
    def get_sample_data(self, sample):
        """Helper method to format sample data"""
        try:
            # Get all field objects from the model
            field_objects = sample.get_field_objects()
            
            # Prepare the sample data with actual field values
            sample_data = {
                'id': sample.id,
                'order': str(sample.order)  # Convert Decimal to string for JSON serialization
            }
            
            # Add all custom fields from the table
            for field_object in field_objects:
                field_name = field_object['field'].name
                field_type = field_object['type'].type
                
                try:
                    field_value = getattr(sample, f'field_{field_object["field"].id}')
                    
                    # Convert field value based on its type
                    if field_value is not None:
                        if field_type == 'number':
                            field_value = float(field_value) if field_value is not None else None
                        elif field_type == 'boolean':
                            field_value = bool(field_value)
                        elif field_type in ['date', 'last_modified', 'created_on']:
                            field_value = field_value.isoformat() if field_value else None
                        elif field_type in ['created_by', 'last_modified_by'] or str(type(field_value).__name__) == 'User':
                            # Handle User objects
                            if hasattr(field_value, 'email'):
                                field_value = {
                                    'id': field_value.id,
                                    'email': field_value.email,
                                    'first_name': getattr(field_value, 'first_name', ''),
                                    'last_name': getattr(field_value, 'last_name', '')
                                }
                            else:
                                field_value = {'id': field_value.id, 'value': str(field_value)}
                        elif field_type == 'link_row':
                            # Handle Baserow link table relationships
                            if field_value:
                                if hasattr(field_value, 'all'):
                                    # Many-to-many relationship - get all related objects
                                    related_items = []
                                    for related_obj in field_value.all():
                                        # Try to get a meaningful display value
                                        display_value = str(related_obj.id)
                                        # Look for common display fields
                                        for attr in ['name', 'title', 'display_name', 'value']:
                                            if hasattr(related_obj, f'field_{attr}'):
                                                try:
                                                    attr_value = getattr(related_obj, f'field_{attr}')
                                                    if attr_value:
                                                        display_value = str(attr_value)
                                                        break
                                                except:
                                                    continue
                                        related_items.append({'id': related_obj.id, 'value': display_value})
                                    field_value = related_items
                                elif hasattr(field_value, 'id'):
                                    # Single relationship
                                    display_value = str(field_value.id)
                                    # Look for common display fields
                                    for attr in ['name', 'title', 'display_name', 'value']:
                                        if hasattr(field_value, f'field_{attr}'):
                                            try:
                                                attr_value = getattr(field_value, f'field_{attr}')
                                                if attr_value:
                                                    display_value = str(attr_value)
                                                    break
                                            except:
                                                continue
                                    field_value = {'id': field_value.id, 'value': display_value}
                                else:
                                    field_value = None
                    
                    sample_data[field_name] = field_value
                except Exception as e:
                    logger.warning(f"Could not get field {field_name}: {str(e)}")
                    sample_data[field_name] = None
            
            # Add timestamps
            sample_data.update({
                'created_on': sample.created_on.isoformat() if sample.created_on else None,
                'updated_on': sample.updated_on.isoformat() if sample.updated_on else None
            })
            
            return sample_data
            
        except Exception as e:
            logger.error(f"Error getting sample data: {str(e)}")
            raise

    def get(self, request, sample_id=None):
        """
        GET /api/basetest/sample/ - List all samples
        GET /api/basetest/sample/{id}/ - Get single sample
        """
        try:
            model, _ = self.get_model_and_table()
            
            # Get single sample
            if sample_id:
                sample = model.objects.get(id=sample_id)
                return Response({
                    "status": "success",
                    "sample": self.get_sample_data(sample)
                })
            
            # Get all samples
            samples = model.objects.all()
            samples_data = [self.get_sample_data(sample) for sample in samples]
            
            return Response({
                "status": "success",
                "count": len(samples_data),
                "samples": samples_data
            })
            
        except model.DoesNotExist:
            return Response({"error": "Sample not found"}, status=404)
        except Database.DoesNotExist:
            return Response({"error": "Database 'Hublms' not found"}, status=404)
        except Table.DoesNotExist:
            return Response({"error": "Table 'Sampler' not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        """
        POST /api/basetest/sample/ - Create a new sample
        """
        try:
            model, table = self.get_model_and_table()
            data = request.data
            
            # Get field mappings
            field_objects = {}
            for field_obj in model.get_field_objects():
                field_name = field_obj['field'].name
                field_objects[field_name] = field_obj
            
            # Prepare sample data with field mappings
            sample_data = {}
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
                    
                    sample_data[f'field_{field_id}'] = value
            
            # Create the sample
            sample = model.objects.create(**sample_data)
            
            return Response({
                "status": "success",
                "message": "Sample created successfully",
                "sample": self.get_sample_data(sample)
            }, status=201)
            
        except Exception as e:
            import traceback
            logger.error(f"Error creating sample: {str(e)}\\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)
    
    def put(self, request, sample_id):
        """
        PUT /api/basetest/sample/{id}/ - Update a sample
        """
        try:
            model, table = self.get_model_and_table()
            
            # Get the sample to update
            sample = model.objects.get(id=sample_id)
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
                    
                    setattr(sample, f'field_{field_id}', value)
            
            # Save changes
            sample.save()
            
            return Response({
                "status": "success",
                "message": "Sample updated successfully",
                "sample": self.get_sample_data(sample)
            })
            
        except model.DoesNotExist:
            return Response({"error": "Sample not found"}, status=404)
        except Exception as e:
            import traceback
            logger.error(f"Error updating sample: {str(e)}\\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)
    
    def delete(self, request, sample_id):
        """
        DELETE /api/basetest/sample/{id}/ - Delete a sample
        """
        try:
            model, table = self.get_model_and_table()
            
            # Get the sample to delete
            sample = model.objects.get(id=sample_id)
            sample_data = self.get_sample_data(sample)  # Get data before deletion
            
            # Delete the sample
            sample.delete()
            
            return Response({
                "status": "success",
                "message": "Sample deleted successfully",
                "deleted_sample": sample_data
            })
            
        except model.DoesNotExist:
            return Response({"error": "Sample not found"}, status=404)
        except Exception as e:
            import traceback
            logger.error(f"Error deleting sample: {str(e)}\\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)


class EnrolmentsView(APIView):
    permission_classes = (AllowAny,)
    
    def get_model_and_table(self):
        """Helper method to get the model and table"""
        database = Database.objects.get(name="Hublms")
        table = Table.objects.get(database=database, name="Enrolments")
        model = table.get_model()
        return model, table
    
    def get_enrollment_data(self, enrollment):
        """Helper method to format enrollment data with course and student info"""
        try:
            # Get all field objects from the model
            field_objects = enrollment.get_field_objects()
            
            # Prepare the enrollment data with actual field values
            enrollment_data = {
                'id': enrollment.id,
                'order': str(enrollment.order)  # Convert Decimal to string for JSON serialization
            }
            
            # Add all custom fields from the table
            for field_object in field_objects:
                field_name = field_object['field'].name
                field_type = field_object['type'].type
                
                try:
                    field_value = getattr(enrollment, f'field_{field_object["field"].id}')
                    
                    # Convert field value based on its type
                    if field_value is not None:
                        if field_type == 'number':
                            field_value = float(field_value) if field_value is not None else None
                        elif field_type == 'boolean':
                            field_value = bool(field_value)
                        elif field_type in ['date', 'last_modified', 'created_on']:
                            field_value = field_value.isoformat() if field_value else None
                        elif field_type in ['created_by', 'last_modified_by'] or str(type(field_value).__name__) == 'User':
                            # Handle User objects
                            if hasattr(field_value, 'email'):
                                field_value = {
                                    'id': field_value.id,
                                    'email': field_value.email,
                                    'first_name': getattr(field_value, 'first_name', ''),
                                    'last_name': getattr(field_value, 'last_name', '')
                                }
                            else:
                                field_value = {'id': field_value.id, 'value': str(field_value)}
                        elif field_type == 'link_row':
                            # Handle Baserow link table relationships (Courses and Student links)
                            if field_value:
                                if hasattr(field_value, 'all'):
                                    # Many-to-many relationship - get all related objects
                                    related_items = []
                                    for related_obj in field_value.all():
                                        # Get detailed info for linked objects
                                        related_data = self.get_linked_object_data(related_obj, field_name)
                                        related_items.append(related_data)
                                    field_value = related_items
                                elif hasattr(field_value, 'id'):
                                    # Single relationship - get detailed info
                                    field_value = self.get_linked_object_data(field_value, field_name)
                                else:
                                    field_value = None
                        else:
                            # Fallback for any other complex objects
                            try:
                                # Try to convert to a basic type for JSON serialization
                                if hasattr(field_value, '__dict__'):
                                    # Complex object - convert to string representation
                                    field_value = str(field_value)
                            except:
                                field_value = str(field_value)
                    
                    enrollment_data[field_name] = field_value
                except Exception as e:
                    logger.warning(f"Could not get field {field_name}: {str(e)}")
                    enrollment_data[field_name] = None
            
            # Add timestamps
            enrollment_data.update({
                'created_on': enrollment.created_on.isoformat() if enrollment.created_on else None,
                'updated_on': enrollment.updated_on.isoformat() if enrollment.updated_on else None
            })
            
            return enrollment_data
            
        except Exception as e:
            logger.error(f"Error getting enrollment data: {str(e)}")
            raise

    def get_linked_object_data(self, linked_obj, field_name):
        """Get detailed data for linked objects (Courses, Students)"""
        try:
            # Get all fields from the linked object
            linked_field_objects = linked_obj.get_field_objects()
            
            linked_data = {
                'id': linked_obj.id,
                'order': str(linked_obj.order) if hasattr(linked_obj, 'order') else None
            }
            
            # Add all fields from the linked object
            for linked_field_obj in linked_field_objects:
                linked_field_name = linked_field_obj['field'].name
                linked_field_type = linked_field_obj['type'].type
                
                try:
                    linked_field_value = getattr(linked_obj, f'field_{linked_field_obj["field"].id}')
                    
                    # Convert field value based on its type
                    if linked_field_value is not None:
                        if linked_field_type == 'number':
                            linked_field_value = float(linked_field_value) if linked_field_value is not None else None
                        elif linked_field_type == 'boolean':
                            linked_field_value = bool(linked_field_value)
                        elif linked_field_type in ['date', 'last_modified', 'created_on']:
                            linked_field_value = linked_field_value.isoformat() if linked_field_value else None
                        elif linked_field_type in ['created_by', 'last_modified_by'] or str(type(linked_field_value).__name__) == 'User':
                            # Handle User objects in linked data
                            if hasattr(linked_field_value, 'email'):
                                linked_field_value = {
                                    'id': linked_field_value.id,
                                    'email': linked_field_value.email,
                                    'first_name': getattr(linked_field_value, 'first_name', ''),
                                    'last_name': getattr(linked_field_value, 'last_name', '')
                                }
                            else:
                                linked_field_value = {'id': linked_field_value.id, 'value': str(linked_field_value)}
                        else:
                            # Simple conversion for other types
                            try:
                                if hasattr(linked_field_value, '__dict__'):
                                    linked_field_value = str(linked_field_value)
                            except:
                                linked_field_value = str(linked_field_value)
                    
                    linked_data[linked_field_name] = linked_field_value
                except Exception as e:
                    logger.warning(f"Could not get linked field {linked_field_name}: {str(e)}")
                    linked_data[linked_field_name] = None
            
            # Add timestamps for linked object
            linked_data.update({
                'created_on': linked_obj.created_on.isoformat() if linked_obj.created_on else None,
                'updated_on': linked_obj.updated_on.isoformat() if linked_obj.updated_on else None
            })
            
            return linked_data
            
        except Exception as e:
            logger.warning(f"Error getting linked object data: {str(e)}")
            return {'id': linked_obj.id, 'value': str(linked_obj)}

    def get(self, request, enrollment_id=None):
        """
        GET /api/basetest/enrolments/ - List all enrollments
        GET /api/basetest/enrolments/{id}/ - Get single enrollment
        GET /api/basetest/enrolments/student/{student_id}/ - Get enrollments for specific student
        """
        try:
            model, _ = self.get_model_and_table()
            
            # Check if this is a student-specific request
            student_id = request.GET.get('student_id')
            if student_id:
                # Filter enrollments by student
                enrollments = model.objects.all()
                student_enrollments = []
                
                for enrollment in enrollments:
                    enrollment_data = self.get_enrollment_data(enrollment)
                    # Check if Student field contains the requested student ID
                    student_field = enrollment_data.get('Student')
                    if student_field:
                        # Handle both single student and list of students
                        if isinstance(student_field, list):
                            # Check if any student in the list matches
                            for student in student_field:
                                if str(student.get('id')) == str(student_id):
                                    student_enrollments.append(enrollment_data)
                                    break
                        elif isinstance(student_field, dict):
                            # Single student object
                            if str(student_field.get('id')) == str(student_id):
                                student_enrollments.append(enrollment_data)
                
                return Response({
                    "status": "success",
                    "count": len(student_enrollments),
                    "student_id": student_id,
                    "enrollments": student_enrollments
                })
            
            # Get single enrollment
            if enrollment_id:
                enrollment = model.objects.get(id=enrollment_id)
                return Response({
                    "status": "success",
                    "enrollment": self.get_enrollment_data(enrollment)
                })
            
            # Get all enrollments
            enrollments = model.objects.all()
            enrollments_data = [self.get_enrollment_data(enrollment) for enrollment in enrollments]
            
            return Response({
                "status": "success",
                "count": len(enrollments_data),
                "enrollments": enrollments_data
            })
            
        except model.DoesNotExist:
            return Response({"error": "Enrollment not found"}, status=404)
        except Database.DoesNotExist:
            return Response({"error": "Database 'Hublms' not found"}, status=404)
        except Table.DoesNotExist:
            return Response({"error": "Table 'Enrolments' not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        """
        POST /api/basetest/enrolments/ - Create a new enrollment
        """
        try:
            model, table = self.get_model_and_table()
            data = request.data
            
            # Get field mappings
            field_objects = {}
            many_to_many_fields = {}
            regular_fields = {}
            
            for field_obj in model.get_field_objects():
                field_name = field_obj['field'].name
                field_type = field_obj['type'].type
                field_id = field_obj['field'].id
                
                if field_type == 'link_row' and hasattr(model, f'field_{field_id}'):
                    many_to_many_fields[field_name] = field_obj
                else:
                    regular_fields[field_name] = field_obj
            
            # Prepare regular field data
            enrollment_data = {}
            m2m_data = {}
            
            for field_name, value in data.items():
                if field_name in many_to_many_fields:
                    field_obj = many_to_many_fields[field_name]
                    field_id = field_obj['field'].id
                    m2m_data[f'field_{field_id}'] = value
                elif field_name in regular_fields:
                    field_obj = regular_fields[field_name]
                    field_id = field_obj['field'].id
                    field_type = field_obj['type'].type
                    
                    # Convert value based on field type
                    if value is not None:
                        if field_type == 'number':
                            value = float(value) if value != '' else None
                        elif field_type == 'boolean':
                            value = bool(value)
                    
                    enrollment_data[f'field_{field_id}'] = value
            
            # Create the enrollment with regular fields first
            enrollment = model.objects.create(**enrollment_data)
            
            # Handle many-to-many relationships after the initial save
            for field_name, value in m2m_data.items():
                if value is not None:
                    if hasattr(enrollment, field_name):
                        # Get the related manager and set the related objects
                        related_manager = getattr(enrollment, field_name)
                        if hasattr(related_manager, 'set'):
                            # Convert single ID to list if needed
                            related_ids = [value] if isinstance(value, (int, str)) else value
                            related_manager.set(related_ids)
            
            # Refresh the instance to get the updated relationships
            enrollment.refresh_from_db()
            
            return Response({
                "status": "success",
                "message": "Enrollment created successfully",
                "enrollment": self.get_enrollment_data(enrollment)
            }, status=201)
            
        except Exception as e:
            import traceback
            logger.error(f"Error creating enrollment: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)
    
    def put(self, request, enrollment_id):
        """
        PUT /api/basetest/enrolments/{id}/ - Update an enrollment
        """
        try:
            model, table = self.get_model_and_table()
            
            # Get the enrollment to update
            enrollment = model.objects.get(id=enrollment_id)
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
                    
                    setattr(enrollment, f'field_{field_id}', value)
            
            # Save changes
            enrollment.save()
            
            return Response({
                "status": "success",
                "message": "Enrollment updated successfully",
                "enrollment": self.get_enrollment_data(enrollment)
            })
            
        except model.DoesNotExist:
            return Response({"error": "Enrollment not found"}, status=404)
        except Exception as e:
            import traceback
            logger.error(f"Error updating enrollment: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)
    
    def delete(self, request, enrollment_id):
        """
        DELETE /api/basetest/enrolments/{id}/ - Delete an enrollment
        """
        try:
            model, table = self.get_model_and_table()
            
            # Get the enrollment to delete
            enrollment = model.objects.get(id=enrollment_id)
            enrollment_data = self.get_enrollment_data(enrollment)  # Get data before deletion
            
            # Delete the enrollment
            enrollment.delete()
            
            return Response({
                "status": "success",
                "message": "Enrollment deleted successfully",
                "deleted_enrollment": enrollment_data
            })
            
        except model.DoesNotExist:
            return Response({"error": "Enrollment not found"}, status=404)
        except Exception as e:
            import traceback
            logger.error(f"Error deleting enrollment: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)


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


class ObtainJSONWebTokens(TokenObtainPairView):
    """
    Custom JWT token view that authenticates against Baserow Users table
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
            401: get_error_schema([
                "ERROR_INVALID_CREDENTIALS",
                "ERROR_DEACTIVATED_USER",
                "ERROR_AUTH_PROVIDER_DISABLED",
                "ERROR_EMAIL_VERIFICATION_REQUIRED",
            ]),
        },
        auth=[],
    )
    @map_exceptions({
        AuthenticationFailed: ERROR_INVALID_CREDENTIALS,
        DeactivatedUserException: ERROR_DEACTIVATED_USER,
        AuthProviderDisabled: ERROR_AUTH_PROVIDER_DISABLED,
        EmailVerificationRequired: ERROR_EMAIL_VERIFICATION_REQUIRED,
    })
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)