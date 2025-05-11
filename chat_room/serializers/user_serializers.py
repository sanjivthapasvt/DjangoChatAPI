from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Basic serializer to return limited user info
class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile_pic']
        read_only_fields = ['id', 'username', 'email'] 
