from django.contrib import admin

# Register your models here.
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Custom user model admin
    """
    list_display = ('id', 'username', 'email', 'role', 'phone_number', 'is_phone_verified')
    list_display_links = ('id', 'username', 'email')
    list_filter = ('role', 'is_phone_verified')
    search_fields = ('username', 'email')
    ordering = ('id',)
    readonly_fields = ('id',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'is_phone_verified')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    ordering = ('id',)
    readonly_fields = ('id',)
    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ('role', 'is_phone_verified')
    search_fields = ('username', 'email')
    ordering = ('id',)
    readonly_fields = ('id',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'is_phone_verified')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
