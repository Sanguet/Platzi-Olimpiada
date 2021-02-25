
"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from foodyplus.users.permissions import IsAccountOwner

# Serializers
from foodyplus.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    AccountVerificationSerializer,
    ProfileModelSerializer,
    ChangePasswordSerializer,
    EmailPasswordSerializer,
    ResetPasswordSerializer
)

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Models
from foodyplus.users.models import User, Profile


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """User login API view."""
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('username', 'email', 'is_verified',
                     'is_active')
    ordering_fields = ('username', 'email', 'is_verified',
                       'is_active')
    ordering = ()
    filter_fields = ('username', 'email', 'is_verified',
                     'is_active')

    def get_permissions(self):
        """Asigna permisos dependiendo de la accion"""
        if self.action in ['signup', 'login', 'verify', 'email_password', 'reset_password']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated]
        elif self.action in ['create', 'list']:
            permissions = [IsAuthenticated]
        elif self.action in ['change_password']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_queryset(self):
        """Devolvemos el queryset modificado"""
        queryset = User.objects.all()
        queryset = queryset.filter(is_active=True)
        return queryset

    @action(detail=False, methods=["post"])
    def login(self, request):
        """Handle HTTP POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def signup(self, request):
        """User sign up API view."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def verify(self, request):
        """Account verification API view."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulation, now go to management!'}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def change_password(self, request):
        """Account verification API view."""
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        password = serializer.save()
        data = {
            'message': 'Felicidades, la contraseña a sido cambiada con exito!',
            'Tu nueva contraseña es': password
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def email_password(self, request):
        """Account verification API view."""
        serializer = EmailPasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {
            'message': 'El email se envio con exito!',
            'Usuario': UserModelSerializer(user).data
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def reset_password(self, request):
        """Account verification API view."""
        serializer = ResetPasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        password = serializer.save()
        data = {
            'message': 'La contraseña se reseteo con exito!',
            'Contraseña': password
        }
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response."""
        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        profile = Profile.objects.get(
            user=request.user,
        )
        data = {
            'user': response.data,
            'profile': ProfileModelSerializer(profile, many=False).data
        }
        response.data = data
        return response

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
