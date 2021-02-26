# Django REST Framework
from rest_framework import viewsets

# Serializers
from foodyplus.foods.serializers import LabelModelSerializer

# Models
from foodyplus.foods.models import Label

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from foodyplus.foods.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class LabelViewSet(viewsets.ModelViewSet):

    serializer_class = LabelModelSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ()
    filter_fields = ('name',)

    def get_permissions(self):
        """Asignamos los permisos en base a las acciones."""
        permissions = [IsAuthenticated, IsAdminUser]
        if self.action in ['list']:
            permissions = []
        return [permission() for permission in permissions]

    def get_queryset(self):
        queryset = Label.objects.all()
        queryset = queryset.filter(is_active=True)
        return queryset
