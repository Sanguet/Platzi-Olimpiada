# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import Label


class LabelModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    name = serializers.CharField()

    class Meta:
        """Meta class"""

        model = Label
        fields = (
            'id',
            'name',
        )
        read_only_fields = (
            'id',
        )

    def validate_name(self, data):
        """Validamos el nombre"""
        # Verificamos que el nombre no se repita
        try:
            Label.objects.get(name=data)
            raise serializers.ValidationError('1025: Ya existe un label con ese nombre')
        except Label.DoesNotExist:
            return data

        return data
