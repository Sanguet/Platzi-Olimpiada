# Django REST Framework
from rest_framework import viewsets

# Serializers
from foodyplus.users.serializers import ShippingInfoModelSerializer

# Models
from foodyplus.users.models import ShippingInfo

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from foodyplus.users.permissions import IsUserAdmin, IsAccountOwner
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)


class ShippingInfoViewSet(viewsets.ModelViewSet):

    serializer_class = ShippingInfoModelSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('id', 'first_name', 'last_name', 'country',
                     'street_address', 'apartament', 'city', 'state', 'zip_code')
    ordering_fields = ('country', 'city', 'state', 'zip_code')
    ordering = ()
    filter_fields = ('first_name', 'last_name', 'country', 'street_address', 'apartament', 'city', 'state', 'zip_code')

    def get_permissions(self):
        """Asigna permisos dependiendo de la accion"""
        permissions = [AllowAny]
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated, IsAccountOwner]
        elif self.action in ['list', ]:
            permissions = [IsAuthenticated, IsUserAdmin]
        return [p() for p in permissions]

    def get_queryset(self):
        user = self.request.user
        queryset = ShippingInfo.objects.all()
        if user.account_type == 'A':
            queryset = queryset.filter(is_active=True)
        else:
            queryset = queryset.filter(user=user, is_active=True)

        return queryset
