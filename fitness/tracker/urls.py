from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FitnessDataViewSet, ActivityTypeViewSet, ActivitySummaryViewSet

router = DefaultRouter()
router.register(r'fitness', FitnessDataViewSet, basename='fitness-data')
router.register(r'activity', ActivityTypeViewSet, basename='activity-type')
router.register(r'summary', ActivitySummaryViewSet, basename='activity-summary')

urlpatterns = [
    path('', include(router.urls)),
]