from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    weight= models.FloatField(null=True, blank=True)