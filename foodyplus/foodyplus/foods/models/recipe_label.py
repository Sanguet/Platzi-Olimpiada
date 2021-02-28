# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class RecipeLabel(BasicModel):
    """ Modelo de las etiquetas de la receta

    Extiende de BasicModel para las metricas
    """
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    label = models.ForeignKey('Label', on_delete=models.CASCADE)
