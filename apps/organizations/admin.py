from django.contrib import admin

from apps.core.admin import BaseAdmin
from .models import Organization


class OrganizationMemberInline(admin.TabularInline):
    model = Organization.members.through
    extra = 1


@admin.register(Organization)
class OrganizationAdmin(BaseAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    inlines = [OrganizationMemberInline]
