# Django REST Framework
from rest_framework import viewsets

# Serializers
from foodyplus.foods.serializers import PlanningModelSerializer

# Models
from foodyplus.foods.models import Planning

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from foodyplus.users.permissions import IsUserAdmin, IsAccountOwner
from rest_framework.permissions import IsAuthenticated, AllowAny


class PlanningViewSet(viewsets.ModelViewSet):

    serializer_class = PlanningModelSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('user', 'detail', 'name', 'date', 'description')
    ordering_fields = ('user', 'name', 'date')
    ordering = ()
    filter_fields = ('user', 'detail', 'name', 'date', 'description')

    def get_permissions(self):
        """Asigna permisos dependiendo de la accion"""
        permissions = [AllowAny]
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated, IsAccountOwner]
        elif self.action in ['list', 'create']:
            permissions = [IsAuthenticated, IsUserAdmin]
        return [p() for p in permissions]

    def get_queryset(self):
        user = self.request.user
        queryset = Planning.objects.all()
        if user.account_type == 'A':
            queryset = queryset.filter(is_active=True)
        else:
            queryset = queryset.filter(user=user, is_active=True)

        return queryset
