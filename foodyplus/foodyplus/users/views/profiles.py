# Django REST Framework
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

# Serializers
from foodyplus.users.serializers import ProfileModelSerializer

# Models
from foodyplus.users.models import Profile

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from foodyplus.users.permissions import IsThisOwner
from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):

    serializer_class = ProfileModelSerializer
    permissions = [IsAuthenticated, IsThisOwner]

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ()
    ordering_fields = ()
    ordering = ()
    filter_fields = ()

    def get_queryset(self):
        queryset = Profile.objects.all()
        queryset = queryset.filter(user=self.request.user, is_active=True)
        return queryset

    def destroy(self, request, pk=None):
        raise MethodNotAllowed('DELETE')

    def create(self, request, pk=None):
        raise MethodNotAllowed('CREATE')
