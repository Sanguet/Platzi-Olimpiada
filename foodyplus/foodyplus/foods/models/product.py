# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class Product(BasicModel):
    """ Modelo de los productos

    Extiende de BasicModel para las metricas
    """

    product_category = models.ForeignKey(
        "ProductCategory",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    name = models.CharField(
        "Nombre del producto",
        max_length=100
    )

    cost = models.DecimalField(
        "Costo del producto",
        max_digits=19,
        decimal_places=2
    )

    price = models.DecimalField(
        "Precio del producto",
        max_digits=19,
        decimal_places=2
    )

    stock = models.DecimalField(
        "Inventario del producto",
        max_digits=19,
        decimal_places=2,
        default=1000
    )

    provider = models.CharField(
        "Nombre del proveedor",
        max_length=50,
        null=True,
        blank=True
    )

    barcode = models.BigIntegerField(
        "Codigo del producto",
        null=True,
        blank=True
    )

    discount = models.DecimalField(
        "Descuento del producto",
        blank=True,
        max_digits=19,
        decimal_places=2,
        default=0
    )

    units_sales = models.IntegerField(
        'Numero de ventas hechas de este producto en el mes',
        blank=True,
        default=0
    )

    unit = models.CharField(
        "Unidad de venta",
        max_length=10,
        null=True,
        blank=True
    )

    def __str__(self):
        """Regresa el nombre del producto"""
        return self.name
