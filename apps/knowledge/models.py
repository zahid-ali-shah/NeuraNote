from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from simple_history.models import HistoricalRecords

from apps.core.models import TimestampModel
from apps.users.models import User
from apps.workspaces.models import Workspace


class Knowledge(MPTTModel, TimestampModel):
    TYPE_CHOICES = (
        ('note', 'Note'),
        ('link', 'Link'),
        ('quote', 'Quote'),
        ('folder', 'Folder'),
        ('article', 'Article'),
    )
    VISIBILITY_CHOICES = (
        ('private', 'Private'),
        ('workspace', 'Workspace'),
        ('org', 'Organization'),
        ('public', 'Public'),
    )
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    knowledge_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='knowledge')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    visibility = models.CharField(max_length=50, choices=VISIBILITY_CHOICES, default='private')
    shared_with = models.ManyToManyField(User, blank=True, related_name='shared_knowledge')
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    history = HistoricalRecords()

    class MPTTMeta:
        order_insertion_by = ['name']
