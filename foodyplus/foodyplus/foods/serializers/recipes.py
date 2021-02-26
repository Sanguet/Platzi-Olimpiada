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
            'country', 'total_time', 'likes', 'portions', 'detail', 'label'
        )
        read_only_fields = (
            'id',
        )

        depth = 1

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
        """Creacion de la receta"""
        # Sacamos los datos que ya tenemos en el context
        data.pop('recipe_category')

        # Creamos la receta
        recipe = Recipe.objects.create(
            recipe_category=self.context['recipe_category'],
            **data
        )

        return recipe

    def update(self, data, instance):
        # Validamos que el dato existe, sino lo ponemos como estaba
        try:
            self.context['recipe_category']
        except KeyError:
            self.context['recipe_category'] = instance.recipe_category

        # Hacemos update de los datos que existen y sino los dejamos como estaban
        instance.recipe_category = self.context['recipe_category']
        instance.name = data.get('name', instance.name)
        instance.video = data.get('video', instance.video)
        instance.utensils = data.get('utensils', instance.utensils)
        instance.country = data.get('country', instance.country)
        instance.total_time = data.get('total_time', instance.total_time)
        instance.likes = data.get('likes', instance.likes)
        instance.portions = data.get('portions', instance.portions)
        instance.description = data.get('description', instance.description)
        instance.comment = data.get('comment', instance.comment)

        instance.save()

        return instance
