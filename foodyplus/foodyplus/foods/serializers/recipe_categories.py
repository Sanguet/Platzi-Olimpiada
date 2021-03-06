# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import RecipeCategory


class RecipeCategoryModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    name = serializers.CharField()

    class Meta:
        """Meta class"""

        model = RecipeCategory
        fields = (
            'id',
            'name', 'comment',
            'icon'
        )
        read_only_fields = (
            'id',
        )

    def validate_name(self, data):
        """Validamos el nombre"""
        # Verificamos que el nombre no se repita para un mismo usuario
        try:
            RecipeCategory.objects.get(name=data)
            raise serializers.ValidationError('1025: Ya existe una categoría de producto con ese nombre')
        except RecipeCategory.DoesNotExist:
            return data

        return data
