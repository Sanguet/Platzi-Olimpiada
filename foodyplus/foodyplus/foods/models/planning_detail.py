# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class PlanningDetail(BasicModel):
    """ Modelo del detalle de la planificacion

    Tabla intermedia de muchos a muchos entre
    recipe y planning
    """

    planning = models.ForeignKey('Planning', on_delete=models.CASCADE)

    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)

    day = models.DateTimeField(
        "Dia de la semana o del mes"
    )

    TIME_TYPES = (
        ('D', 'Desayuno'),
        ('A', 'Almuerzo'),
        ('M', 'Merienda'),
        ('C', 'Cena'),
    )

    time = models.CharField(
        "Tipo de planificacion",
        max_length=1,
        choices=TIME_TYPES,
    )
