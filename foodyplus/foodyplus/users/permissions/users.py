# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Permite el acceso del objeto solo al dueño o el admin"""
    message = '1101: Solo el usuario o admin tienen permiso'

    def has_object_permission(self, request, view, obj):
        """Checkea que el usuario sea igual al objeto"""
        user = request.user
        return (user == obj or user.account_type == "A")


class IsUserAdmin(BasePermission):
    """Permite el acceso al admin"""
    message = '1103: Solo el administrador de la cuenta tiene permiso para ejecutar esta accion'

    def has_permission(self, request, view):
        """Solo le damos permiso al admin"""
        user = request.user
        return user.account_type == "A"


class IsThisOwner(BasePermission):
    """Permite el acceso del objeto solo al usuario del perfil y al admin"""
    message = '1102: Solo el usuario del perfil o el admin de la cuenta pueden ejecutar esta accion'

    def has_object_permission(self, request, view, obj):
        """Checkea que el usuario sea igual al objeto"""
        user = request.user
        if user == obj.user:
            return True
        else:
            return False
