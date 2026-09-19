from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        null=True,
        blank=True,
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    password = models.CharField()