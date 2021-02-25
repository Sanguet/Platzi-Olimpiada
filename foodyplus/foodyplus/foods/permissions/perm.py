from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    """Permiso para los usuarios que son admin"""
    message = '1103: Solo el administrador puede ejecutar esta accion'

    def has_permission(self, request, view):
        """Solo le damos permiso al admin"""
        user = request.user
        if user.account_type == "A":
            return True
        else:
            return False


class IsClientUser(permissions.BasePermission):
    """Permiso para los usuarios que son clientes o superiores"""
    message = '1105: Solo clientes o superiores pueden ejecutar esta accion'

    def has_permission(self, request, view):
        """Solo le damos permiso a clientes o superiores"""
        user = request.user
        if user.account_type == "C" or user.account_type == "A":
            return True
        else:
            return False


class IsThisAccount(permissions.BasePermission):
    """Permiso para los usuarios que estan dentro del objeto"""
    message = '1106: Necesitas que tu usuario este dentro del objeto'

    def has_permission(self, request, view):
        """Pasamos el objeto al permiso"""
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        """Solo permitimos el acceso a usuarios que estan dentro del objeto"""
        user = request.user
        return user == obj.user or user.account_type == "A"
