# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import Coupon

# Utils
import random
from string import ascii_uppercase, digits

# Validators
from foodyplus.foods.validators import Validators


class CouponModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    user = serializers.CharField()

    class Meta:
        """Meta class"""

        model = Coupon
        fields = (
            'id',
            'user', 'name',
            'code', 'discount'
        )
        read_only_fields = (
            'id', 'code'
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

        # Creamos el cupon
        coupon = Coupon.objects.create(
            user=user,
            code=code,
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
