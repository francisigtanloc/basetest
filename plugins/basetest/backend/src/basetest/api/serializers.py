from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from baserow.core.user.utils import normalize_email_address
from basetest.authentication import BaserowUserBackend


class NormalizedEmailField(serializers.EmailField):
    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return normalize_email_address(data)


class LmsTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom token serializer that authenticates against Baserow Users table
    """
    email = NormalizedEmailField(required=True)
    password = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the default username field since we're using email
        if 'username' in self.fields:
            del self.fields['username']

    def validate(self, attrs):
        """
        Validate credentials against Baserow Users table
        """
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError({
                'detail': 'Email and password are required.'
            })

        # Use our custom Baserow authentication backend
        backend = BaserowUserBackend()
        user = backend.authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if user is None:
            raise AuthenticationFailed(
                'No active account found with the given credentials'
            )

        # Create the token payload
        refresh = RefreshToken()
        refresh['user_id'] = user.id
        refresh['email'] = getattr(user, 'email', email)
        
        # Add user data to the response
        user_data = {
            'id': user.id,
            'email': getattr(user, 'email', email),
            'name': getattr(user, 'first_name', ''),
            'is_active': getattr(user, 'is_active', True)
        }

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user_data
        }