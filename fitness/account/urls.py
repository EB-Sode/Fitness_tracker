from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterUserViewSet

#routers
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'register', RegisterUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
