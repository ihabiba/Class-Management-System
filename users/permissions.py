from rest_framework.permissions import BasePermission

class IsStaff(BasePermission):
    """
    Allows access only to staff users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "staff")

from rest_framework.permissions import BasePermission

class IsProfessor(BasePermission):
    """
    Allows access only to professor users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "professor")
