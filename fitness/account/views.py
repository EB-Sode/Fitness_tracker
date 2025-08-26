from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import UserSerializer, RegisterUserSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny, IsAuthenticated
from tracker.permissions import IsOwnerOrReadOnly

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, IsAuthenticated, IsOwnerOrReadOnly]

class RegisterUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]