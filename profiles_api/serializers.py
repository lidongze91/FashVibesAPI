from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'bio', 'web', 'full_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name'],
            bio=validated_data['bio'],
            web=validated_data['web'],
            full_name=validated_data['full_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user