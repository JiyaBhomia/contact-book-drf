#
# REPLACE the entire contents of this file
#
from rest_framework import serializers
from .models import Contact
from django.contrib.auth.models import User  # <-- Add this import

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'address', 'notes', 'created_at']

#
# ADD THIS NEW CLASS
# This is the UserSerializer that was missing
#
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # This handles password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user