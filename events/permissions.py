from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # allow all users to read data
            return True
        else:
            # only allow administrators to modify data
            return request.user.is_authenticated and request.user.is_staff