from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', '남성'), ('female', '여성')], blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.username
