from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.core.admin import BaseAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseAdmin, UserAdmin):
    list_display = ('username', 'email', 'created_at', 'updated_at')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
