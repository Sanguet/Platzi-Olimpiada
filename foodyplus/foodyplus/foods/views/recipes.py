# Django REST Framework
from rest_framework import viewsets

# Serializers
from foodyplus.foods.serializers import RecipeModelSerializer

# Models
from foodyplus.foods.models import Recipe

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from foodyplus.foods.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class RecipeViewSet(viewsets.ModelViewSet):

    serializer_class = RecipeModelSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('recipe_category__name', 'description', 'name', 'video', 'utensils',
                     'country', 'total_time', 'likes', 'portions', 'detail__id', 'label__name', 'preparation', 'tips')
    ordering = ('country', 'total_time', 'likes', 'portions')
    filter_fields = ('recipe_category', 'description', 'name', 'video', 'utensils',
                     'country', 'total_time', 'likes', 'portions', 'detail', 'label')

    def get_permissions(self):
        """Asignamos los permisos en base a las acciones."""
        permissions = [IsAuthenticated, IsAdminUser]
        if self.action in ['list']:
            permissions = []
        return [permission() for permission in permissions]

    def get_queryset(self):
        queryset = Recipe.objects.all()
        queryset = queryset.filter(is_active=True)
        return queryset

    def perform_destroy(self, instance):
        """Solo desactivamos la venta"""
        # Delete
        instance.is_active = False
        instance.save()
