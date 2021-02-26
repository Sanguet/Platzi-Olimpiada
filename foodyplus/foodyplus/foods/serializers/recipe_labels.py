# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import RecipeLabel

# Validators
from foodyplus.foods.validators import Validators


class RecipeLabelModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    label = serializers.CharField()

    class Meta:
        """Meta class"""

        model = RecipeLabel
        fields = (
            'id',
            'recipe', 'label'
        )
        read_only_fields = (
            'id',
        )

    def validate_label(self, data):
        """Validador individual del label"""
        user = self.context['request'].user
        self.context['label'] = Validators.label(pk=data, user=user)
        return data

    def create(self, data):
        """Creacion del label en el receta"""
        # Obtenemos los datos del contexto
        sale = self.context['sale']
        label = self.context['label']

        # Creamos el label en la receta
        recipe_label = RecipeLabel.objects.create(
            sale=sale,
            label=label
        )

        return recipe_label
