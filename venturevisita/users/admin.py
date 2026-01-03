from django.contrib import admin
from .models import User, AuthToken


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'phone', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('date_joined',)
    exclude = ('password',)


@admin.register(AuthToken)
class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    search_fields = ('key', 'user__username', 'user__email')
