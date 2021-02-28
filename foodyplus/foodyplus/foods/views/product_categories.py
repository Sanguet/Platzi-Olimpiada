# Django REST Framework
from rest_framework import viewsets

# Serializers
from foodyplus.foods.serializers import ProductCategoryModelSerializer

# Models
from foodyplus.foods.models import ProductCategory

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from foodyplus.foods.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class ProductCategoryViewSet(viewsets.ModelViewSet):

    serializer_class = ProductCategoryModelSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name', 'comment',)
    ordering_fields = ('name', 'comment', 'usages')
    ordering = ()
    filter_fields = ('name', 'comment')

    def get_permissions(self):
        """Asignamos los permisos en base a las acciones."""
        permissions = [IsAuthenticated, IsAdminUser]
        if self.action in ['list']:
            permissions = []
        return [permission() for permission in permissions]

    def get_queryset(self):
        queryset = ProductCategory.objects.all()
        queryset = queryset.filter(is_active=True)
        return queryset
