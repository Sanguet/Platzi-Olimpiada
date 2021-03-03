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
        "Nombre del cupon",
        max_length=100
    )

    code = models.CharField(
        "Codigo del cupon",
        max_length=13,
        unique=True
    )

    discount = models.DecimalField(
        "Descuento del cupon",
        max_digits=19,
        decimal_places=2,
    )

    exp_date = models.DateTimeField(
        "Fecha de expiracion",
    )
