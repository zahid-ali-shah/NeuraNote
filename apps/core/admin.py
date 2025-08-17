from django.conf import settings
from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return settings.DEBUG  # Allow in local, disable in prod

    def has_change_permission(self, request, obj=None):
        return settings.DEBUG

    def has_delete_permission(self, request, obj=None):
        return settings.DEBUG

    def has_view_permission(self, request, obj=None):
        return True  # View-only in prod
