# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import Sale, Product, ProductCategory


class Validators():
    """Validadores usados en foods"""

    def sale(pk):
        """Validador del campo sale

        pk es un String
        """
        try:
            sale = Sale.objects.get(id=int(pk))
        except Sale.DoesNotExist:
            raise serializers.ValidationError('1034: Venta no encontrada')
        return sale

    def product(pk):
        """Validador del campo product

        pk es un String
        """
        try:
            product = Product.objects.get(id=int(pk))
        except Product.DoesNotExist:
            raise serializers.ValidationError('1035: Producto no encontrado')
        return product

    def product_category(pk):
        """Validador del campo product_category

        pk es un String
        """
        try:
            product_category = ProductCategory.objects.get(id=int(pk))
        except ProductCategory.DoesNotExist:
            raise serializers.ValidationError('1036: Categoria del producto no encontrado')
        return product_category
