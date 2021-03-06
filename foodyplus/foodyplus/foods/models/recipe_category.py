# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class RecipeCategory(BasicModel):
    """ Modelo de la categoria de los recetas

    Extiende de BasicModel para las metricas
    """

    name = models.CharField(
        "Nombre de la categoria",
        max_length=100,
        unique=True
    )

    comment = models.TextField(
        'Comentario de la categoria',
        max_length=500,
        blank=True
    )

    icon = models.ImageField(
        "Imagen de la categoria",
        upload_to="foods/pictures/",
        blank=True,
        null=True
    )

    def __str__(self):
        """Regresa el nombre de la categoria"""
        return self.name
