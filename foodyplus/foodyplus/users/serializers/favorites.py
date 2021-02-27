# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.users.models import Favorite

# Validators
from foodyplus.foods.validators import Validators


class FavoriteModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    recipe = serializers.CharField()

    class Meta:
        """Meta class"""

        model = Favorite
        fields = (
            'id',
            'user', 'recipe'
        )
        read_only_fields = (
            'id', 'user'
        )

    def validate_recipe(self, data):
        """Validador individual del label"""
        self.context['recipe'] = Validators.recipe(pk=data)
        return data

    def create(self, data):
        """Creacion del label en el receta"""
        # Obtenemos los datos del contexto
        user = self.context['user']
        recipe = self.context['recipe']

        # Creamos el label en la receta
        favorite = Favorite.objects.create(
            user=user,
            recipe=recipe
        )

        # Agregamos un like a la receta
        recipe.likes += 1
        recipe.save()

        return favorite
