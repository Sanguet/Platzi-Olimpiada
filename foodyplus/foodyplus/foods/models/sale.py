# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class Sale(BasicModel):
    """ Modelo de Venta

    Extiende de BasicUserModel para las metricas y usuario
    """

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    coupon = models.ForeignKey(
        "Coupon",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    detail = models.ManyToManyField(
        "Product",
        through="SaleDetail",
        through_fields=("sale", "product")
    )

    PAYMENT_TYPES = (
        ('G', 'Gratis'),
        ('C', 'Contado'),
        ('D', 'Debito'),
        ('T', 'Credito')
    )

    payment_method = models.CharField(
        "Tipo de metodo de pago",
        default="C",
        max_length=1,
        choices=PAYMENT_TYPES,
        blank=True,
    )

    total = models.DecimalField(
        "Total",
        blank=True,
        default=0,
        max_digits=19,
        decimal_places=2
    )

    delivery_date = models.DateTimeField(
        'Fecha en la que debe ser entregado',
    )

    STEP_TYPES = (
        ('P', 'Preparandose'),
        ('E', 'En camino'),
        ('R', 'Recibido'),
    )

    steps = models.CharField(
        'Seguimiento de la venta',
        default="P",
        max_length=1,
        choices=STEP_TYPES,
        blank=True,
    )

    comment = models.TextField(
        'Comentario de la venta',
        max_length=500,
        blank=True
    )

    def __str__(self):
        """Regresa el id de la venta"""
        return str(self.id)
