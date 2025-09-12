from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterUserCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#routers
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserCreateView.as_view(), name='register-user'),

    #session auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #token auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
