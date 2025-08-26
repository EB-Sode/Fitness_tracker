from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FitnessDataViewSet, ActivityTypeViewSet

router = DefaultRouter()
router.register(r'fitness', FitnessDataViewSet)
router.register(r'activity', ActivityTypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]