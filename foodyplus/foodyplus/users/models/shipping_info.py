# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class ShippingInfo(BasicModel):
    """Modelo del perfil

    El modelo del perfil contiene su data publica, como biografia, imagen y estadistica
    """

    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    first_name = models.CharField(
        "Nombre del perfil",
        max_length=30,
    )

    last_name = models.CharField(
        "Apellido del perfil",
        max_length=30,
    )

    country = models.CharField(
        "Pais donde vive",
        max_length=30,
    )

    street_address = models.CharField(
        "Direccion de la calle",
        max_length=30,
    )

    apartament = models.CharField(
        "Apartamente donde vive",
        max_length=30,
        blank=True,
        null=True
    )

    city = models.CharField(
        "Ciudad donde vive",
        max_length=50,
    )

    state = models.CharField(
        "Estado/provincia donde vive",
        max_length=30,
    )

    zip_code = models.IntegerField(
        "Codigo postal",
    )
