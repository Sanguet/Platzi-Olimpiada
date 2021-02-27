# Django REST Framework
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

# Serializers
from foodyplus.foods.serializers import SaleModelSerializer

# Models
from foodyplus.foods.models import Sale

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from foodyplus.foods.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class SaleViewSet(viewsets.ModelViewSet):

    serializer_class = SaleModelSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('detail', 'payment_method', 'user',
                     'total', 'comment', 'shipping_info', 'coupon', 'delivery_date', 'steps')
    ordering_fields = ('detail', 'payment_method', 'user',
                       'shipping_info', 'coupon', 'delivery_date', 'steps')
    ordering = ()
    filter_fields = ('detail', 'payment_method', 'user',
                     'total', 'comment', 'shipping_info', 'coupon', 'delivery_date', 'steps')

    def get_permissions(self):
        """Asignamos los permisos en base a las acciones."""
        permissions = [IsAuthenticated, IsAdminUser]
        if self.action in ['create']:
            permissions = []
        return [permission() for permission in permissions]

    def get_queryset(self):
        user = self.request.user
        queryset = Sale.objects.all()
        if user.account_type == 'A':
            queryset = queryset.filter(is_active=True)
        else:
            queryset = queryset.filter(user=user, is_active=True)

        return queryset

    def perform_destroy(self, instance):
        """Solo desactivamos la venta"""
        # Delete
        instance.is_active = False
        instance.save()

    def update(self, request, pk=None):
        raise MethodNotAllowed('UPDATE')
