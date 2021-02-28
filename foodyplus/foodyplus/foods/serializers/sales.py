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
import random
from string import ascii_uppercase, digits


class SaleModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    class Meta:
        """Meta class"""

        model = Sale
        fields = (
            'id', 'user', 'payment_method',
            'comment', 'shipping_info', 'discount',
            'delivery_date', 'steps', 'total', 'detail',
            'delivery_charge', 'tracking_code'
        )
        read_only_fields = (
            'id', 'user', 'delivery_date',
            'tracking_code'
        )

    def create(self, data):
        """Creacion de la venta"""
        # Sacamos los datos que ya tenemos en el context
        user = self.context['request'].user
        tracking_code = SucesionAleatoria()

        # Horario de entrega
        now = timezone.now() - timedelta(hours=3)
        next_week = now + timedelta(days=7)
        delivery_date = next_week

        # Creamos la venta
        if user.is_authenticated:
            sale = Sale.objects.create(
                user=user,
                delivery_date=delivery_date,
                tracking_code=tracking_code,
                **data
            )
        else:
            sale = Sale.objects.create(
                delivery_date=delivery_date,
                tracking_code=tracking_code,
                **data
            )

        return sale


class TrackingSerializer(serializers.Serializer):
    """Recuperamos el estado del seguimiento de la venta"""
    tracking_code = serializers.CharField(min_length=20, max_length=20)

    def save(self):
        """En base al codigo buscamos la venta"""
        try:
            sale = Sale.objects.get(tracking_code=self.data['tracking_code'], is_active=True)
        except Sale.DoesNotExist:
            raise serializers.ValidationError('No se encontro ninguna venta con ese codigo de seguimiento')

        sale_step = sale.steps

        return sale_step


def SucesionAleatoria():
    CODE_LENGTH = 20
    pool = ascii_uppercase + digits
    code = random.choices(pool, k=CODE_LENGTH)
    code = "".join(code)
    return code
