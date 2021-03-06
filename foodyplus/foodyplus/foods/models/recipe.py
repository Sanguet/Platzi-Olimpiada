# Django
from django.db import models

# Utils
from foodyplus.utils.models import BasicModel


class Recipe(BasicModel):
    """ Modelo de las recetas

    Extiende de BasicModel para las metricas
    """

    recipe_category = models.ForeignKey(
        "RecipeCategory",
        on_delete=models.SET_NULL,
        null=True
    )

    detail = models.ManyToManyField(
        "Product",
        through="RecipeDetail",
        through_fields=("recipe", "product")
    )

    comment = models.ManyToManyField(
        "users.User",
        through="RecipeComment",
        through_fields=("recipe", "user")
    )

    name = models.CharField(
        "Nombre de la receta",
        max_length=100
    )

    picture = models.ImageField(
        "Imagen de la receta",
        upload_to="foods/pictures/",
        blank=True,
        null=True
    )

    video = models.URLField(
        'Link del video de la receta',
        max_length=1000,
        blank=True,
        null=True
    )

    country = models.CharField(
        'Pais de origen de la receta',
        max_length=50,
        blank=True,
        default='Internacional'
    )

    total_time = models.DecimalField(
        'Tiempo que se demora en preparar la receta',
        blank=True,
        max_digits=19,
        decimal_places=2,
        default=1
    )

    likes = models.IntegerField(
        'Numero de likes que tiene la receta',
        blank=True,
        default=0
    )

    portions = models.IntegerField(
        'Numero de raciones',
        blank=True,
        null=True
    )

    description = models.TextField(
        'Descripcion de la receta',
        max_length=4000,
    )

    preparation = models.TextField(
        'Preparacion de la receta',
        max_length=4000,
    )

    price = models.DecimalField(
        "Precio",
        max_digits=19,
        decimal_places=2,
        blank=True,
        null=True
    )

    def __str__(self):
        """Regresa el nombre de la etiqueta"""
        return str(self.name)
