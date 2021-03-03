# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404

# Serializers
from foodyplus.users.serializers import FavoriteModelSerializer

# Models
from foodyplus.users.models import Favorite, User

# Permissions
from foodyplus.users.permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated


class FavoriteViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    "Favorite view set"

    serializer_class = FavoriteModelSerializer
    permissions = [IsAuthenticated, IsAccountOwner]

    def dispatch(self, request, *args, **kwargs):
        """Verificamos que la receta exista"""
        user = kwargs['user_pk']
        self.user = get_object_or_404(User, id=user)
        return super(FavoriteViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer_context(self):
        """ Añadimos user al contexto del serializer"""
        context = super(FavoriteViewSet, self).get_serializer_context()
        context['user'] = self.user
        return context

    def get_queryset(self):
        """Retorno el queryset de Favorite"""
        queryset = Favorite.objects.filter(
            user_id=self.user,
            is_active=True,
        )
        return queryset

    def perform_destroy(self, instance):
        """Solo desactivamos la venta"""
        # Sacar likes
        recipe = instance.recipe
        recipe.likes -= 1
        recipe.save()

        # Delete
        instance.delete()
