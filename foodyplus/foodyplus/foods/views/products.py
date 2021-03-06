# Django REST Framework
from rest_framework import viewsets

# Serializers
from foodyplus.foods.serializers import ProductModelSerializer

# Models
from foodyplus.foods.models import Product

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from foodyplus.foods.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductModelSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name', 'cost', 'price', 'stock', 'provider', 'barcode', 'units_sales')
    ordering_fields = ('name', 'cost', 'price', 'stock', 'provider')
    ordering = ()
    filter_fields = ('name', 'cost', 'price', 'stock', 'provider',
                     'barcode', 'product_category', 'units_sales')

    def get_permissions(self):
        """Asignamos los permisos en base a las acciones."""
        permissions = [IsAuthenticated, IsAdminUser]
        if self.action in ['list']:
            permissions = []
        return [permission() for permission in permissions]

    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = queryset.filter(is_active=True)
        return queryset
