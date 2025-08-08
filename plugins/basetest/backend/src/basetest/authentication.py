from django.contrib.auth.backends import BaseBackend
from baserow.contrib.database.models import Database
from baserow.contrib.database.table.models import Table
import logging

logger = logging.getLogger(__name__)


class BaserowUserBackend(BaseBackend):
    """
    Custom authentication backend for Baserow Users table
    """

    def get_users_model_and_table(self):
        """Helper method to get the Baserow Users table model"""
        try:
            # First try to find the database - it could be "Admin's workspace" or similar
            database = None
            possible_names = ["Admin's workspace", "Hublms", "workspace"]
            
            for db_name in possible_names:
                try:
                    database = Database.objects.get(name=db_name)
                    logger.info(f"Found database: {db_name}")
                    break
                except Database.DoesNotExist:
                    continue
            
            if not database:
                # If no specific name matches, get the first available database
                database = Database.objects.first()
                if database:
                    logger.info(f"Using first available database: {database.name}")
            
            if not database:
                logger.error("No database found")
                return None, None
                
            table = Table.objects.get(database=database, name="Users")
            model = table.get_model()
            logger.info(f"Successfully got Users table from database: {database.name}")
            return model, table
        except Table.DoesNotExist:
            logger.error(f"Users table not found in database: {database.name if database else 'Unknown'}")
            return None, None
        except Exception as e:
            logger.error(f"Error getting Users table: {str(e)}")
            return None, None

    def get_field_mappings(self, model):
        """Get field mappings for the Users table"""
        field_mappings = {}
        for field_obj in model.get_field_objects():
            field_name = field_obj['field'].name.lower()
            field_id = field_obj['field'].id
            field_mappings[field_name] = field_id
        return field_mappings

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticate against the Baserow Users table using email only
        """
        if username is None:
            return None

        try:
            model, table = self.get_users_model_and_table()
            if not model:
                logger.error("Could not get Users table model")
                return None
                
            field_mappings = self.get_field_mappings(model)
            
            # Find the user by email
            email_field_id = field_mappings.get('email')
            if not email_field_id:
                logger.error("Email field not found in Users table")
                return None
                
            # Query for user by email
            user = model.objects.filter(**{f'field_{email_field_id}': username}).first()
            
            if not user:
                logger.warning(f"User not found with email: {username}")
                return None
            
            # Get the active field value (skip password check for now)
            active_field_id = field_mappings.get('active')
            is_active = getattr(user, f'field_{active_field_id}', True) if active_field_id else True
            
            # Debug logging
            logger.info(f"Authentication attempt for {username}")
            logger.info(f"User found in database: {user.id}")
            logger.info(f"User is active: {is_active}")
            
            # Check if user is active
            if not is_active:
                logger.warning(f"User {username} is not active")
                return None
            
            # Skip password check - just authenticate if email exists and user is active
            logger.info(f"Email-only authentication successful for {username}")
            
            # Create a user-like object with required authentication properties
            user._meta.app_label = 'basetest'
            user.email = getattr(user, f'field_{email_field_id}')
            user.username = user.email
            
            # Get name field if available
            name_field_id = field_mappings.get('name')
            if name_field_id:
                user.first_name = getattr(user, f'field_{name_field_id}', '')
            else:
                user.first_name = ''
            
            user.is_active = is_active
            user.is_authenticated = True
            user.is_anonymous = False
            
            logger.info(f"Successfully authenticated user: {username}")
            return user
                
        except Exception as e:
            logger.error(f"Error during authentication: {str(e)}")
            return None

    def get_user(self, user_id):
        """
        Get user by ID from Baserow Users table
        """
        try:
            model, table = self.get_users_model_and_table()
            if not model:
                return None
                
            user = model.objects.filter(id=user_id).first()
            if user:
                field_mappings = self.get_field_mappings(model)
                
                # Set user properties
                email_field_id = field_mappings.get('email')
                name_field_id = field_mappings.get('name')
                active_field_id = field_mappings.get('active')
                
                if email_field_id:
                    user.email = getattr(user, f'field_{email_field_id}')
                    user.username = user.email
                
                if name_field_id:
                    user.first_name = getattr(user, f'field_{name_field_id}', '')
                
                if active_field_id:
                    user.is_active = getattr(user, f'field_{active_field_id}', True)
                else:
                    user.is_active = True
                    
                user.is_authenticated = True
                user.is_anonymous = False
                
                return user
                
        except Exception as e:
            logger.error(f"Error getting user by ID {user_id}: {str(e)}")
            return None
            
        return None
