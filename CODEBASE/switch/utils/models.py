# Django
from django.db import models


class StockModel(models.Model):
    """ Modelo basico abstracto.

    StockModel  es una clase abstracta de la que heredan
    todos los modelos de User de la API. Esta clase provee
    los siguientes atributos:
    + created (DateTime): Almacena la fecha de creacion
    + modified (DateTime): Almacena la fecha de modificacion
    + is_active (Boolean): Si esta activo el valor o no
    """

    created = models.DateTimeField(
        "created at",
        auto_now_add=True,
        help_text="Date Time de la creacion del objeto"
    )
    modified = models.DateTimeField(
        "modified at",
        auto_now=True,
        help_text="Date Time de la ultima modificacion del objeto"
    )

    is_active = models.BooleanField(
        "is active",
        default=True,
        blank=True,
        help_text="La fila esta activa o no"
    )

    class Meta:
        """ Opciones del meta """

        abstract = True

        get_latest_by = "created"
        ordering = ["-created", "modified"]


class ManagementModel(models.Model):
    """ Modelo basico abstracto.

    ManagementModel  es una clase abstracta de la que heredan
    todos los modelos de Management de la API. Esta clase provee
    los siguientes atributos:
    + created (DateTime): Almacena la fecha de creacion
    + modified (DateTime): Almacena la fecha de modificacion
    + modified_by (Foreing Key): Almacena el perfil del cambio
    + is_active (Boolean): Si esta activo el valor o no
    + user (Foreing Key): Almacena el usuario a quien pertenece
    """

    created = models.DateTimeField(
        "created at",
        auto_now_add=True,
        help_text="Date Time de la creacion del objeto"
    )
    modified = models.DateTimeField(
        "modified at",
        auto_now=True,
        help_text="Date Time de la ultima modificacion del objeto"
    )

    modified_by = models.ForeignKey(
        "users.Profile",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Usuario de creación',
        help_text="Quien fue el que lo modifico"
    )

    is_active = models.BooleanField(
        "is active",
        default=True,
        blank=True,
        help_text="La fila esta activa o no"
    )

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        """ Opciones del meta """

        abstract = True

        get_latest_by = "created"
        ordering = ["-created", "modified"]
