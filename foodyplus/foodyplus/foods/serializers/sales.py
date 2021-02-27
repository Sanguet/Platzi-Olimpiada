# Django
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import Sale

# Validators
from foodyplus.foods.validators import Validators

# Utils
from datetime import date
from datetime import timedelta


class SaleModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    class Meta:
        """Meta class"""

        model = Sale
        fields = (
            'id', 'user', 'payment_method',
            'comment', 'shipping_info', 'discount',
            'delivery_date', 'steps', 'total', 'detail',
            'delivery_charge'
        )
        read_only_fields = (
            'id', 'user', 'delivery_date'
        )

    def create(self, data):
        """Creacion de la venta"""
        # Sacamos los datos que ya tenemos en el context
        user = self.context['request'].user

        # Horario de entrega
        now = timezone.now() - timedelta(hours=3)
        next_week = now + timedelta(days=7)
        delivery_date = next_week

        # Creamos la venta
        if user.is_authenticated:
            sale = Sale.objects.create(
                user=user,
                delivery_date=delivery_date,
                **data
            )
        else:
            sale = Sale.objects.create(
                delivery_date=delivery_date,
                **data
            )

        return sale
