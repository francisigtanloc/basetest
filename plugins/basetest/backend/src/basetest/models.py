from django.contrib.auth.hashers import make_password, check_password
from django.db import models


class LmsUsers(models.Model):
    """
    Custom LMS Users table for authentication
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=128)
    status = models.CharField(max_length=50, default='active')

    class Meta:
        db_table = 'lms_users'
        verbose_name = 'LMS User'
        verbose_name_plural = 'LMS Users'

    def __str__(self):
        return f"{self.name} ({self.email})"

    def set_password(self, raw_password):
        """Hash and set the password"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Check if the provided password matches the stored password"""
        return check_password(raw_password, self.password)

    @property
    def is_active(self):
        """Check if user is active based on status field"""
        return self.status.lower() == 'active'

    @property
    def is_authenticated(self):
        """Always return True for authenticated users"""
        return True

    @property
    def is_anonymous(self):
        """Always return False for authenticated users"""
        return False
