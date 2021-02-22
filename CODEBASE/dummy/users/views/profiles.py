# Django REST Framework
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

# Serializers
from dummy.users.serializers import ProfileModelSerializer

# Models
from dummy.users.models import Profile

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from dummy.users.permissions import IsThisOwner
from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):

    serializer_class = ProfileModelSerializer
    permissions = [IsAuthenticated, IsThisOwner]

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('first_name', 'last_name', 'points')
    ordering_fields = ('first_name', 'last_name', 'points')
    ordering = ()
    filter_fields = ('first_name', 'last_name', 'points')

    def get_queryset(self):
        queryset = Profile.objects.all()
        queryset = queryset.filter(user=self.request.user, is_active=True)
        return queryset

    def destroy(self, request, pk=None):
        raise MethodNotAllowed('DELETE')

    def create(self, request, pk=None):
        raise MethodNotAllowed('CREATE')
