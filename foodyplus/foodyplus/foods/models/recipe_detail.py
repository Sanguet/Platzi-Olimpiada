# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class RecipeDetail(BasicModel):
    """ Modelo de la tabla intermedia entre recetas y productos

    Extiende de BasicModel para las metricas
    """

    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
