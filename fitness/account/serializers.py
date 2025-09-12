from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser


CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_no', 'weight', 'age', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    