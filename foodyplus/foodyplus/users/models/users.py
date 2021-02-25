# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utils
from foodyplus.utils.models import BasicModel


class User(BasicModel, AbstractUser):
    """ Modelo de usuario

    Extiende del modelo StockModel y AbstractUser,
    """
    email = models.EmailField(
        "Direccion de email",
        unique=True,
        error_messages={
            "unique": "Ya existe un usuario con este email"
        }
    )

    phone_regex = RegexValidator(
        regex=r"\+?1?\d{9,15}$",
        message="El numero de celular tiene que tener el formato: +999999999. Hasta 15 digitos"
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )

    is_verified = models.BooleanField(
        "Verificado",
        default=True,
        help_text="Se setea a True cuando el email es verificado"
    )

    is_active = models.BooleanField(
        "is active",
        default=True,
        blank=True,
        help_text="La fila esta activa o no"
    )

    ACCOUNT_TYPES = (
        ('G', 'Gratis'),
        ('I', 'Inicial'),
        ('A', 'Avanzado'),
        ('P', 'Premium')
    )

    account_type = models.CharField(
        "Tipo de cuenta",
        default="G",
        max_length=1,
        choices=ACCOUNT_TYPES,
        blank=True,
        null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", ]
