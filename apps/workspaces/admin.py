from django.contrib import admin

from apps.core.admin import BaseAdmin
from .models import Workspace


class WorkspaceMemberInline(admin.TabularInline):
    model = Workspace.members.through
    extra = 1


@admin.register(Workspace)
class WorkspaceAdmin(BaseAdmin):
    list_display = ('name', 'organization', 'is_public', 'created_at', 'updated_at')
    list_filter = ('is_public', 'organization')
    search_fields = ('name',)
    inlines = [WorkspaceMemberInline]
