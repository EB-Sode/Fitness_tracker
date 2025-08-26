from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FitnessDataViewSet, ActivityTypeViewSet, ActivitySummaryViewSet

router = DefaultRouter()
router.register(r'fitness', FitnessDataViewSet)
router.register(r'activity', ActivityTypeViewSet)
router.register(r'summary', ActivitySummaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]