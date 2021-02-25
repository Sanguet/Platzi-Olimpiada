# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class WishList(BasicModel):
    """ Modelo de la lista de deseo

    Tabla intermedia de muchos a muchos entre
    recipes y users
    """

    users = models.ForeignKey('users.User', on_delete=models.CASCADE)

    recipes = models.ForeignKey('Recipe', on_delete=models.CASCADE)
