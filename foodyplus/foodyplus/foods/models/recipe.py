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

    label = models.ManyToManyField(
        "Label",
        through="RecipeLabel",
        through_fields=("recipe", "label")
    )

    name = models.CharField(
        "Nombre de la receta",
        max_length=100
    )

    video = models.URLField(
        'Link del video de la receta',
        max_length=500,
        blank=True,
        null=True
    )

    utensils = models.TextField(
        'Utencilios utilizados',
        max_length=500,
        blank=True,
        null=True
    )

    country = models.CharField(
        'Pais de origen de la receta',
        max_length=50,
        blank=True,
        null=True
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
        max_length=700,
        blank=True,
        null=True
    )

    comment = models.TextField(
        'Comentario de la receta',
        max_length=700,
        blank=True,
        null=True
    )
