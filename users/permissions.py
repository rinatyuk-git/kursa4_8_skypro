from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка на Создателя."""
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
