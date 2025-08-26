from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}({self.phone_no}) is {self.age} years old and weighs {self.weight}"