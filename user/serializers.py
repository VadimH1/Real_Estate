from rest_framework import serializers
from .models import User,Profile

from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'uuid_number'
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            # 'first_name',
            # 'last_name',
            # 'email',
            'user_profile',
            'avatar',
            'phone_number'
        )
   
