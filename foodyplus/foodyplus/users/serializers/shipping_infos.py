# Django REST Framework
from rest_framework import serializers

# Models
from foodyplus.users.models import ShippingInfo


class ShippingInfoModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = ShippingInfo
        fields = (
            'id', 'user', 'first_name',
            'last_name', 'country',
            'street_address', 'apartament',
            'city', 'state', 'zip_code'
        )

        read_only_fields = (
            'id', 'user'
        )

    def create(self, data):
        """Creacion de la informacion de venta"""
        # Sacamos los datos que ya tenemos en el context
        user = self.context['request'].user

        # Creamos la inforamcion de envio
        if user.is_authenticated:
            shipping_info = ShippingInfo.objects.create(
                user=user,
                **data
            )
        else:
            shipping_info = ShippingInfo.objects.create(
                **data
            )

        return shipping_info
