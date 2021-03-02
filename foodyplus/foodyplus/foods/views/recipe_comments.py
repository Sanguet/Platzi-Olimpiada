# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404

# Serializers
from foodyplus.foods.serializers import RecipeCommentModelSerializer

# Models
from foodyplus.foods.models import RecipeComment, Recipe

# Permissions
from foodyplus.foods.permissions import IsThisAccount
from rest_framework.permissions import IsAuthenticated


class RecipeCommentViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    "RecipeComment view set"

    serializer_class = RecipeCommentModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verificamos que la receta exista"""
        recipe = kwargs['recipe_pk']
        self.recipe = get_object_or_404(Recipe, id=recipe)
        return super(RecipeCommentViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer_context(self):
        """ Añadimos recipe al contexto del serializer"""
        context = super(RecipeCommentViewSet, self).get_serializer_context()
        context['recipe'] = self.recipe
        return context

    def get_permissions(self):
        """Asignamos los permisos en base a las acciones."""
        permissions = [IsAuthenticated, IsThisAccount]
        if self.action in ['list']:
            permissions = []
        if self.action in ['create']:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Retorno el queryset de RecipeComment"""
        queryset = RecipeComment.objects.filter(
            recipe_id=self.recipe,
            is_active=True,
        )
        return queryset
