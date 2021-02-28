# Django
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import Coupon

# Validators
from foodyplus.foods.validators import Validators

# Utils
import random
from string import ascii_uppercase, digits
from datetime import date
from datetime import datetime
from datetime import timedelta


class CouponModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    user = serializers.CharField()

    class Meta:
        """Meta class"""

        model = Coupon
        fields = (
            'id',
            'user', 'name',
            'code', 'discount',
            'exp_date'
        )
        read_only_fields = (
            'id', 'code', 'exp_date'
        )

    def validate_user(self, data):
        """Validacion del campo user"""
        self.context['user'] = Validators.user(username=data)
        return data

    def create(self, data):
        """Creacion del cupon"""
        # Obtenemos los datos de user y code
        data.pop('user')
        user = self.context['user']
        code = SucesionAleatoria()

        # Horario de entrega
        now = timezone.now() - timedelta(hours=3)
        exp_date = datetime(year=now.year, month=now.month, day=now.day)

        # Creamos el cupon
        coupon = Coupon.objects.create(
            user=user,
            code=code,
            exp_date=exp_date,
            **data
        )

        return coupon

    def update(self, instance, data):
        """Update del cupon"""
        # Intentamos obtener el nuevo usuario, sino dejamos el que ya estaba
        try:
            user = self.context['user']
        except KeyError:
            user = instance.user

        # Update de la instancia
        instance.user = user
        instance.name = data.get('name', instance.name)
        instance.discount = data.get('discount', instance.discount)
        instance.save()

        return instance


def SucesionAleatoria():
    CODE_LENGTH = 13
    pool = ascii_uppercase + digits
    code = random.choices(pool, k=CODE_LENGTH)
    code = "".join(code)
    return code
