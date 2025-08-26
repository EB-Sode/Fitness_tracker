from django.db import models

# Create your models here.
class ActivityType(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Workout(models.Model):
    activities = models.ManyToManyField(ActivityType, on_delete= models.CASCADE, related_name= 'exercise')
    time = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        activities_list = ", ".join([activity.name for activity in self.activities.all()])
        return f"You will do some {activities_list} on {self.time} for {self.duration}"