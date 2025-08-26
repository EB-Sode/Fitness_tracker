from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, RegisterUserSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]