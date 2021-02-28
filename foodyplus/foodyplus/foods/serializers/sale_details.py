# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import SaleDetail

# Validators
from foodyplus.foods.validators import Validators


class SaleDetailModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    product = serializers.CharField()
    amount = serializers.IntegerField()
    discount = serializers.FloatField(default=0, required=False, min_value=0, max_value=100)

    class Meta:
        """Meta class"""

        model = SaleDetail
        fields = (
            'id',
            'sale', 'product',
            'amount', 'discount',
            'sub_total'
        )
        read_only_fields = (
            'id',
            'sale'
        )

    def validate_product(self, data):
        """Validador individual del product"""
        self.context['product'] = Validators.product(pk=data)
        return data

    def validate(self, data):
        """Validamos los campos que tienen relaciones"""
        # Verificamos que la venta exista
        self.context['sale'] = Validators.sale(pk=self.context['sale'].pk)

        return data

    def create(self, data):
        """Creacion de la venta"""
        # Sacamos los datos que ya tenemos en el context
        data.pop('product')

        # Verificamos si hay stock disponible y lo sacamos
        product = self.context['product']
        if (product.stock - data.get('amount')) >= 0:
            product.stock -= data.get('amount')
            product.save()
        else:
            raise serializers.ValidationError('1026: No tienes suficiente inventario')

        # Creamos el detalle
        sale_detail = SaleDetail.objects.create(
            product=self.context['product'],
            sale=self.context['sale'],
            **data
        )

        # Agregamos el uso a la categoria del producto siempre que sea una venta
        product = self.context['product']
        product_category = product.product_category
        product_category.usages += 1
        product_category.save()

        # Agregamos las ventas al producto
        product.units_sales += 1 * data['amount']
        product.save()

        return sale_detail
