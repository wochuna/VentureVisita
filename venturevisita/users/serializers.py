from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone' 'bio','role']
        
    class UserRegistrationSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['username', 'email', 'phone' 'password', 'role']
        
        def create(self, validated_data):
            validated_data['password'] = make_password(validated_data['password'])
            return super().create(validated_data)