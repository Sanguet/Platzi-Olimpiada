# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import Product

# Validators
from foodyplus.foods.validators import Validators


class ProductModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    product_category = serializers.CharField()
    name = serializers.CharField()
    cost = serializers.DecimalField(max_digits=19, decimal_places=2, min_value=0.00)
    price = serializers.DecimalField(max_digits=19, decimal_places=2, min_value=0.00)
    stock = serializers.IntegerField(min_value=0, default=0)

    class Meta:
        """Meta class"""

        model = Product
        fields = (
            'id', 'modified_by',
            'product_category',
            'name', 'cost',
            'price', 'stock',
            'provider', 'picture',
            'state_line', 'barcode',
            'comment', 'units_sales',
            'is_stock', 'description',
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
        data.pop('product_category')

        # Creamos el producto
        product = Product.objects.create(
            product_category=self.context['product_category'],
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
        instance.comment = data.get('comment', instance.comment)
        instance.description = data.get('description', instance.description)
        instance.picture = data.get('picture', instance.picture)
        instance.discount = data.get('discount', instance.discount)

        instance.save()

        return instance
