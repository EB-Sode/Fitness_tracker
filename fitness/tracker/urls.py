from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FitnessDataViewSet, ActivityTypeViewSet, ActivitySummaryList

router = DefaultRouter()
router.register(r'fitness', FitnessDataViewSet, basename='fitness-data')
router.register(r'activity', ActivityTypeViewSet, basename='activity-type')

urlpatterns = [
    path("summary/", ActivitySummaryList.as_view(), name="activity-summary"),
    path('', include(router.urls)),
]