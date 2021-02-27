# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class Planning(BasicModel):
    """ Modelo de la categoria de la planificacion de comidas

    Extiende de BasicModel para las metricas
    """

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    detail = models.ManyToManyField(
        "Recipe",
        through="PlanningDetail",
        through_fields=("planning", "recipe")
    )

    name = models.CharField(
        "Nombre de la planificacion",
        max_length=100
    )

    DATE_TYPES = (
        ('S', 'Semanal'),
        ('M', 'Mensual')
    )

    date = models.CharField(
        "Tipo de planificacion",
        default="S",
        max_length=1,
        choices=DATE_TYPES,
        blank=True,
    )

    description = models.TextField(
        'Descripcion de la planificacion',
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        """Regresa el nombre de la planificacion"""
        return self.name
