from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterUserViewSet

#routers
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'register', RegisterUserViewSet, basename='register-user')

urlpatterns = [
    path('', include(router.urls)),
]
