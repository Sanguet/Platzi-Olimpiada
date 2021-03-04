# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class ProductCategory(BasicModel):
    """ Modelo de la categoria de los productos

    Extiende de BasicModel para las metricas
    """

    name = models.CharField(
        "Nombre de la categoria",
        unique=True,
        max_length=100
    )

    comment = models.TextField(
        'Comentario de la categoria',
        max_length=500,
        blank=True
    )

    icon_svg = models.TextField(
        'Codigo del icono',
        max_length=500,
    )

    usages = models.IntegerField(
        'Numero de veces que se uso la categoria en el mes',
        blank=True,
        default=0
    )

    def __str__(self):
        """Regresa el nombre de la categoria"""
        return self.name
