# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import RecipeDetail

# Validators
from foodyplus.foods.validators import Validators


class RecipeDetailModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    product = serializers.CharField()
    amount = serializers.IntegerField()
    discount = serializers.FloatField(default=0, required=False, min_value=0, max_value=100)

    class Meta:
        """Meta class"""

        model = RecipeDetail
        fields = (
            'id',
            'recipe', 'product',
            'amount', 'unit',
            'discount', 'sub_total',
        )
        read_only_fields = (
            'id', 'unit',
            'recipe'
        )

    def validate_product(self, data):
        """Validador individual del product"""
        self.context['product'] = Validators.product(pk=data)
        return data

    def create(self, data):
        """Creacion de la venta"""
        # Sacamos los datos que ya tenemos en el context
        data.pop('product')
        unit = self.context['product'].unit

        # Creamos el detalle
        recipe_detail = RecipeDetail.objects.create(
            product=self.context['product'],
            recipe=self.context['recipe'],
            unit=unit,
            **data
        )

        return recipe_detail
