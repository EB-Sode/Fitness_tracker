from rest_framework import viewsets
from .models import FitnessData, ActivityType, ActivitySummary
from .serializers import FitnessDataSerializer, ActivityTypeSerializer, ActivitySummarySerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class FitnessDataViewSet(viewsets.ModelViewSet):
    queryset = FitnessData.objects.all()
    serializer_class = FitnessDataSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        '''override perform_create so the user is automatically set'''
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return FitnessData.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='history')
    def history(self, request):
        """
        Returns the user's activity history with optional filters:
        - ?start_date=YYYY-MM-DD
        - ?end_date=YYYY-MM-DD
        - ?activity_type=running
        """
        queryset = self.get_queryset()

        # Filters
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        activity_type = request.query_params.get('activity_type')

        if start_date:
            queryset = queryset.filter(date__gte=parse_date(start_date))
        if end_date:
            queryset = queryset.filter(date__lte=parse_date(end_date))
        if activity_type:
            queryset = queryset.filter(activity_type__name__iexact=activity_type)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    #filters
    def get_queryset(self):
        return ActivityType.objects.filter(user=self.request.user)

class ActivitySummaryViewSet(viewsets.ModelViewSet):
    queryset = ActivitySummary.objects.all()
    serializer_class = ActivitySummarySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["activity_type", "summary_type", "period_start", "period_end"]

    def get_queryset(self):
        """
        Restrict summaries to the current authenticated user.
        """
        return super().get_queryset().filter(user=self.request.user)
