# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import Product

# Validators
from foodyplus.foods.validators import Validators


class ProductModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    product_category = serializers.CharField(required=False)
    name = serializers.CharField()
    cost = serializers.DecimalField(max_digits=19, decimal_places=2, min_value=0.00)
    price = serializers.DecimalField(max_digits=19, decimal_places=2, min_value=0.00)
    stock = serializers.DecimalField(max_digits=19, decimal_places=2, min_value=0.00)

    class Meta:
        """Meta class"""

        model = Product
        fields = (
            'id',
            'product_category',
            'name', 'cost',
            'price', 'stock', 'unit',
            'provider',
            'barcode', 'units_sales',
            'discount'

        )
        read_only_fields = (
            'id', 'units_sales',

        )

    def validate_product_category(self, data):
        """Validamos el campo product_cateogry"""
        self.context['product_category'] = Validators.product_category(pk=data)
        return data

    def create(self, data):
        """Creacion de la venta"""
        # Sacamos los datos que ya tenemos en el context

        try:
            data.pop('product_category')
            product_category = self.context['product_category']
        except KeyError:
            product_category = None

        # Creamos el producto
        product = Product.objects.create(
            product_category=product_category,
            **data
        )

        return product

    def update(self, instance, data):
        """Cambios al producto"""
        # Validamos que el dato existe, sino lo ponemos como estaba
        try:
            self.context['product_category']
        except KeyError:
            self.context['product_category'] = instance.product_category

        # Hacemos update de los datos que existen y sino los dejamos como estaban
        instance.product_category = self.context['product_category']
        instance.name = data.get('name', instance.name)
        instance.cost = data.get('cost', instance.cost)
        instance.price = data.get('price', instance.price)
        instance.stock = data.get('stock', instance.stock)
        instance.provider = data.get('provider', instance.provider)
        instance.barcode = data.get('barcode', instance.barcode)
        instance.discount = data.get('discount', instance.discount)

        instance.save()

        return instance
