from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from datetime import timedelta
from .models import FitnessData, ActivitySummary


def update_activity_summary(instance):
    """
    Recalculate daily summary whenever FitnessData changes.
    """
    user = instance.user
    activity_type = instance.activity_type
    date = instance.date

    # Aggregate totals for this user and date
    aggregates = FitnessData.objects.filter(
        user=user,
        date=date,
        activity_type=activity_type
    ).aggregate(
        total_duration=Sum("duration"),
        total_calories=Sum("calories_burned"),
        total_distance=Sum("distance"),
    )

    # If nothing left after deletion, remove the summary
    if not aggregates["total_duration"] and not aggregates["total_calories"] and not aggregates["total_distance"]:
        ActivitySummary.objects.filter(
            user=user,
            period_start=date,
            period_end=date,
            activity_type=activity_type,
            summary_type="daily"
        ).delete()
        return

    # Update or create daily summary
    ActivitySummary.objects.update_or_create(
        user=user,
        period_start=date,
        period_end=date,
        activity_type=activity_type,
        summary_type="daily",
        defaults={
            "total_duration": aggregates["total_duration"] or timedelta(),
            "total_calories": aggregates["total_calories"] or 0,
            "total_distance": aggregates["total_distance"] or 0,
        }
    )


@receiver(post_save, sender=FitnessData)
def update_summary_on_save(sender, instance, **kwargs):
    update_activity_summary(instance)


@receiver(post_delete, sender=FitnessData)
def update_summary_on_delete(sender, instance, **kwargs):
    update_activity_summary(instance)
