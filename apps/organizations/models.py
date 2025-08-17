from django.db import models
from apps.core.models import TimestampModel
from apps.users.models import User

class Organization(TimestampModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_organizations')
    members = models.ManyToManyField(User, related_name='organizations')