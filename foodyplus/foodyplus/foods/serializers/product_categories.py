# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import ProductCategory


class ProductCategoryModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    name = serializers.CharField()

    class Meta:
        """Meta class"""

        model = ProductCategory
        fields = (
            'id',
            'name', 'comment',
            'usages',
        )
        read_only_fields = (
            'id', 'usages',
        )

    def validate_name(self, data):
        """Validamos el nombre"""
        # Verificamos que el nombre no se repita para un mismo usuario
        try:
            ProductCategory.objects.get(name=data)
            raise serializers.ValidationError('1025: Ya existe una categoría de producto con ese nombre')
        except ProductCategory.DoesNotExist:
            return data

        return data
