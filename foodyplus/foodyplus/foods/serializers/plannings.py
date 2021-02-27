# Django
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import Planning


class PlanningModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    user = serializers.StringRelatedField(many=False, required=False)

    class Meta:
        """Meta class"""

        model = Planning
        fields = (
            'id', 'user',
            'name', 'date',
            'description', 'detail'
        )
        read_only_fields = (
            'id', 'user'
        )

        depth = 1

    def create(self, data):
        """Creacion de la venta"""
        # Sacamos los datos que ya tenemos en el context
        user = self.context['request'].user

        # Creamos la planificacion
        planning = Planning.objects.create(
            user=user,
            **data
        )

        return planning
