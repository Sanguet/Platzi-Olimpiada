# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import RecipeComment

# Validators
from foodyplus.foods.validators import Validators


class RecipeCommentModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    user = serializers.StringRelatedField(many=False, required=False)
    recipe = serializers.StringRelatedField(many=False, required=False)

    class Meta:
        """Meta class"""

        model = RecipeComment
        fields = (
            'id', 'user',
            'recipe', 'comment'
        )
        read_only_fields = (
            'id', 'user',
            'recipe'
        )

    def create(self, data):
        """Creacion de la venta"""
        # Sacamos los datos que ya tenemos en el context
        user = self.context['request'].user
        recipe = self.context['recipe']

        # Creamos el detalle
        recipe_comment = RecipeComment.objects.create(
            user=user,
            recipe=recipe,
            **data
        )

        return recipe_comment
