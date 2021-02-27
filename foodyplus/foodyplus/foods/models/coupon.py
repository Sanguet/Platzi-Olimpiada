# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class Coupon(BasicModel):
    """ Modelo de las recetas

    Extiende de BasicModel para las metricas
    """

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE
    )

    name = models.CharField(
        "Nombre del producto",
        max_length=100
    )

    code = models.BigIntegerField(
        "Codigo del cupon",
        unique=True
    )

    discount = models.DecimalField(
        "Descuento del cupon",
        blank=True,
        max_digits=19,
        decimal_places=2,
        default=0
    )
