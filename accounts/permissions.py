from rest_framework import permissions

from config_master import ROLE_SUPER_ADMIN


class UserPermissions(permissions.BasePermission):
    """
    This custom permission class is used to determine if a user has permission to perform various actions of a user
    object like create, update, delete
    """
    edit_methods = ("PUT", "PATCH")
    model_change_methods = ("POST", "PUT", "PATCH", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.role == ROLE_SUPER_ADMIN:
            return True

        if request.method not in self.model_change_methods:
            return True

        if int(request.user.role) < int(request.data.get('role', request.user.role)):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.role == ROLE_SUPER_ADMIN:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if int(request.user.role) < int(request.data.get('role', request.user.role)):
            return True

        return False
