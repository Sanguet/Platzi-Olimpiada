# Django REST Framework
from rest_framework import viewsets

# Serializers
from foodyplus.foods.serializers import CouponModelSerializer

# Models
from foodyplus.foods.models import Coupon

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from foodyplus.foods.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class CouponViewSet(viewsets.ModelViewSet):

    serializer_class = CouponModelSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('user', 'name', 'code', 'discount', 'exp_date')
    ordering_fields = ('user', 'name', 'code', 'discount', 'exp_date')
    ordering = ()
    filter_fields = ('user', 'name', 'code', 'discount', 'exp_date')

    def get_permissions(self):
        """Asignamos los permisos en base a las acciones."""
        permissions = [IsAuthenticated, IsAdminUser]
        if self.action in ['list']:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_queryset(self):
        user = self.request.user
        queryset = Coupon.objects.all()
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
