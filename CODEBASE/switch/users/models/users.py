# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utils
from switch.utils.models import StockModel


class User(StockModel, AbstractUser):
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

    company_name = models.CharField(
        "Nombre de la compañia",
        max_length=140,
    )

    company_slug_name = models.SlugField(
        "Nombre de pila de la compañia",
        unique=True,
        max_length=40,
        error_messages={
            "unique": "Ya existe un usuario con este nombre de compañia"
        }
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

    is_admin = models.BooleanField(
        "Admin",
        default=True,
        help_text="Solo hay un admin"
    )

    REQUIRED_FIELDS = ["email", "company_name", "company_slug_name"]

