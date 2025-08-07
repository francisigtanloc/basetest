from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import LmsUsers


class LmsUserBackend(BaseBackend):
    """
    Custom authentication backend for LmsUsers table
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticate against the lms_users table using email and password
        """
        if username is None or password is None:
            return None

        try:
            # Look up user by email in lms_users table
            lms_user = LmsUsers.objects.get(email=username)
            
            # Check if user is active (status = 'active')
            if not lms_user.is_active:
                return None
                
            # Check password
            if lms_user.check_password(password):
                # Return the lms_user object (it has the required authentication properties)
                return lms_user
                
        except LmsUsers.DoesNotExist:
            return None
            
        return None

    def get_user(self, user_id):
        """
        Get user by ID from lms_users table
        """
        try:
            return LmsUsers.objects.get(pk=user_id)
        except LmsUsers.DoesNotExist:
            return None
