# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class RecipeComment(BasicModel):
    """ Modelo de los comentarios de la receta

    Tabla intermedia de muchos a muchos entre
    recipe y user
    """

    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    comment = models.TextField(
        'Comentario de la venta',
        max_length=700,
    )
