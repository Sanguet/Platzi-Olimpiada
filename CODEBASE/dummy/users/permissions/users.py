# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Permite el acceso del objeto solo al dueño o al admin"""
    message = '1101: Solo el administrador de la cuenta tiene permiso para ejecutar esta accion'

    def has_object_permission(self, request, view, obj):
        """Checkea que el usuario sea igual al objeto o que sea admin"""
        user = request.user
        return (user.work_range == 'A' or user.account == obj.account)


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
