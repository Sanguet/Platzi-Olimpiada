# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class Label(BasicModel):
    """ Modelo de la etiqueta

    Extiende de BasicModel para las metricas
    """
    name = models.CharField(
        "Nombre de la etiqueta",
        max_length=100
    )