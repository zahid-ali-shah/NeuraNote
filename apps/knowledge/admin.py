from django.contrib import admin

from apps.core.admin import BaseAdmin
from .models import Knowledge


class KnowledgeSharedWithInline(admin.TabularInline):
    model = Knowledge.shared_with.through
    extra = 1


@admin.register(Knowledge)
class KnowledgeAdmin(BaseAdmin):
    list_display = ('name', 'knowledge_type', 'workspace', 'visibility', 'created_at', 'updated_at')
    list_filter = ('knowledge_type', 'visibility', 'workspace')
    search_fields = ('name', 'content')
    inlines = [KnowledgeSharedWithInline]
