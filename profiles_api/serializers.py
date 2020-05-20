from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):

    """ Serializes a name field for testing Api view """

    name = serializers.CharField(max_length = 10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user Profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password') # fields that are accessible from models
        """ Adding some other options to password field"""
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style' : {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """  Create and return a new user """
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ Serializes Profile Feed Item """
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', "user_profile", 'status_text', 'created_on')
        extra_kwargs = extra_kwargs = {'user_profile':{'read_only':True}}
