from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from apps.core.models import TimestampModel
from apps.organizations.models import Organization
from apps.users.models import User


class Workspace(MPTTModel, TimestampModel):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='workspaces', null=True,
                                     blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_public = models.BooleanField(default=False)
    members = models.ManyToManyField(User, related_name='workspaces', blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']
