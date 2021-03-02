# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404

# Serializers
from foodyplus.foods.serializers import RecipeDetailModelSerializer

# Models
from foodyplus.foods.models import RecipeDetail, Recipe

# Permissions
from foodyplus.foods.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class RecipeDetailViewSet(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    "RecipeDetail view set"

    serializer_class = RecipeDetailModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verificamos que la receta exista"""
        recipe = kwargs['recipe_pk']
        self.recipe = get_object_or_404(Recipe, id=recipe)
        return super(RecipeDetailViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer_context(self):
        """ Añadimos recipe al contexto del serializer"""
        context = super(RecipeDetailViewSet, self).get_serializer_context()
        context['recipe'] = self.recipe
        return context

    def get_permissions(self):
        """Asignamos los permisos en base a las acciones."""
        permissions = [IsAuthenticated, IsAdminUser]
        if self.action in ['list']:
            permissions = []
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Retorno el queryset de RecipeDetail"""
        queryset = RecipeDetail.objects.filter(
            recipe_id=self.recipe,
            is_active=True,
        )
        return queryset
