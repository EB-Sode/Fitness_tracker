from .models import FitnessData, ActivityType, ActivitySummary
from rest_framework import serializers


class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = ['id', 'name']


class FitnessDataSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # show username, don’t allow writing
    activity_type = serializers.SlugRelatedField(
        slug_field='name',
        queryset=ActivityType.objects.all()
    )

    class Meta:
        model = FitnessData
        fields = ['id', 'user', 'activity_type', 'duration', 'calories_burned', 'date', 'duration_in_minutes']


class ActivitySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitySummary
        fields = ['id', 'user', 'activity_type', 'total_duration', 'total_calories', 'total_distance', 'period_start', 'period_end', 'summary_type']

        #some fields read-only since they’re computed via signals
        read_only_fields = ['user', 'period_start', 'period_end', 'summary_type',  'total_duration', 'total_calories', 'total_distance']
