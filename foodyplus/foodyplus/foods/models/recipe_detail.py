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

    amount = models.PositiveIntegerField(
        "Cantidad del producto",
        default=1,
        blank=True
    )

    unit = models.CharField(
        "Unidad de venta",
        max_length=10,
        null=True,
        blank=True
    )

    discount = models.DecimalField(
        "Descuento del producto en la receta",
        blank=True,
        max_digits=19,
        decimal_places=2,
        default=0
    )

    sub_total = models.DecimalField(
        "Sub total",
        max_digits=19,
        decimal_places=2,
    )

    def __str__(self):
        """Regresa el id del detalle"""
        return str(self.pk)
