from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Create your models here.
class ActivityType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)


class FitnessData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fitness_data')
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    duration = models.DurationField()
    calories_burned = models.FloatField(null=True, blank=True)
    date = models.DateField()
    distance = models.FloatField(null=True, blank=True)  # in kilometers, optional

    def __str__(self):
        return f"{self.user.username} did {self.activity_type.name} for {self.duration} on {self.date}"

    class Meta:
        ordering = ['-date']
        unique_together = ('user', 'activity_type', 'date')
    @property
    def duration_in_minutes(self):
        return self.duration.total_seconds() // 60


class ActivitySummary(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='activity_summaries')
    period_start = models.DateField()
    period_end = models.DateField()
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE, blank=True, null=True)  # optional filter
    total_duration = models.DurationField()
    total_calories = models.FloatField()
    total_distance = models.FloatField(blank=True, null=True)
    summary_type = models.CharField(
        max_length=20,
        choices=[("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly"), ("custom", "Custom")]
    )

    class Meta:
        unique_together = ("user", "period_start", "period_end", "activity_type", "summary_type")
        indexes = [models.Index(fields=['user', 'period_start', 'period_end']),]

    def __str__(self):
        return f"{self.user.username} - {self.summary_type} summary ({self.period_start} → {self.period_end})"
