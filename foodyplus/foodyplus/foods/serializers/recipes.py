# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import Recipe

# Validators
from foodyplus.foods.validators import Validators


class RecipeModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    name = serializers.CharField()
    recipe_category = serializers.CharField()

    class Meta:
        """Meta class"""

        model = Recipe
        fields = (
            'id', 'recipe_category', 'description', 'name', 'video', 'utensils',
            'country', 'total_time', 'likes', 'portions'
        )
        read_only_fields = (
            'id'
        )

    def validate_name(self, data):
        """Validamos el nombre"""
        # Verificamos que el nombre no se repita para un mismo usuario
        try:
            Recipe.objects.get(name=data)
            raise serializers.ValidationError('1025: Ya existe una receta con este nombre')
        except Recipe.DoesNotExist:
            return data

        return data

    def validate_recipe_category(self, data):
        """Validamos el campo recipe_cateogry"""
        self.context['recipe_category'] = Validators.recipe_category(pk=data)
        return data

    def create(self, data):
        """Creacion de la venta"""
        # Sacamos los datos que ya tenemos en el context
        data.pop('recipe_category')

        # Creamos la receta
        recipe = Recipe.objects.create(
            recipe_category=self.context['recipe_category'],
            **data
        )

        return recipe
