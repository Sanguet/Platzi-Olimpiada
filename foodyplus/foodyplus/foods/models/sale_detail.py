# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class SaleDetail(BasicModel):
    """ Modelo del detalle de venta

    Tabla intermedia de muchos a muchos entre
    products y sales
    """

    sale = models.ForeignKey('Sale', on_delete=models.CASCADE)

    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    amount = models.PositiveIntegerField(
        "Cantidad del producto",
        default=1,
        blank=True
    )

    discount = models.DecimalField(
        "Descuento del producto",
        blank=True,
        max_digits=19,
        decimal_places=2,
        default=0
    )

    sub_total = models.DecimalField(
        "Sub total",
        blank=True,
        max_digits=19,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        """Regresa la numero de venta y el producto"""
        return str(self.pk)
