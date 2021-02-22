# Django
from django.db import models

# Utils
from dummy.utils.models import UtilModel


class Profile(UtilModel):
    """Modelo del perfil

    El modelo del perfil contiene su data publica, como biografia, imagen y estadistica
    """

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)

    first_name = models.CharField(
        "Nombre del perfil",
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        "Apellido del perfil",
        max_length=30,
        blank=True,
        null=True
    )

    picture = models.ImageField(
        "imagen de perfil",
        upload_to="users/pictures/",
        blank=True,
        null=True
    )

    biografy = models.TextField('Biografia del perfil', max_length=500, blank=True)

    points = models.IntegerField('Cantidad de puntos acumulados', blank=True, default=0)

    def __str__(self):
        """Regresa el nombre del perfil"""
        if self.first_name is None:
            return f'No hay nombre de perfil para el usuario: {self.user} '
        else:
            return self.first_name
