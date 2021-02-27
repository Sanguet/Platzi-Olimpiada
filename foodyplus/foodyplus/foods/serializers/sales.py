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

    coupon = serializers.IntegerField(required=False)

    class Meta:
        """Meta class"""

        model = Sale
        fields = (
            'id', 'user', 'payment_method',
            'comment', 'shipping_info', 'coupon',
            'delivery_date', 'steps', 'total', 'detail'
        )
        read_only_fields = (
            'id', 'user', 'delivery_date'
        )

    def validate_coupon(self, data):
        """Validador individual del cupon"""
        self.context['coupon'] = Validators.coupon(code=data)
        return data

    def create(self, data):
        """Creacion de la venta"""
        # Sacamos los datos que ya tenemos en el context
        user = self.context['request'].user
        try:
            coupon = self.context['coupon']
            data.pop('coupon')
        except KeyError:
            coupon = None

        now = timezone.now() - timedelta(hours=3)

        next_week = now + timedelta(days=7)
        delivery_date = next_week

        # Creamos la venta
        if user.is_authenticated:
            sale = Sale.objects.create(
                user=user,
                coupon=coupon,
                delivery_date=delivery_date,
                **data
            )
        else:
            sale = Sale.objects.create(
                coupon=coupon,
                delivery_date=delivery_date,
                **data
            )

        return sale
