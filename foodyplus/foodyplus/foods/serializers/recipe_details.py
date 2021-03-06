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
            'id', 'sub_total',
            'recipe'
        )

    def validate_product(self, data):
        """Validador individual del product"""
        self.context['product'] = Validators.product_name(name=data)
        return data

    def create(self, data):
        """Creacion de la venta"""
        # Sacamos los datos que ya tenemos en el context
        data.pop('product')
        sub_total = self.context['product'].price * data.get('amount')

        # Creamos el detalle
        recipe_detail = RecipeDetail.objects.create(
            product=self.context['product'],
            recipe=self.context['recipe'],
            sub_total=sub_total,
            **data
        )

        return recipe_detail
