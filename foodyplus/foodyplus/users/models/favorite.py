# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class Favorite(BasicModel):
    """Modelo de las recetas favoritas del usuario
    Extiende de BasicModel para las metricas
    """

    user = models.ForeignKey('User', on_delete=models.CASCADE)

    recipe = models.ForeignKey('foods.Recipe', on_delete=models.CASCADE)
