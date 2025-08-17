from django.contrib.auth.models import AbstractUser
from apps.core.models import TimestampModel
from django.db import models


class User(AbstractUser, TimestampModel):
    email = models.EmailField(unique=True)
