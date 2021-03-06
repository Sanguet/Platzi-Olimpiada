# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import Sale, Product, ProductCategory, RecipeCategory, Coupon, Recipe
from foodyplus.users.models import User


class Validators():
    """Validadores usados en foods"""

    def sale(pk):
        """Validador del campo sale

        pk es un String
        """
        try:
            sale = Sale.objects.get(id=int(pk))
        except Sale.DoesNotExist:
            raise serializers.ValidationError('1034: Venta no encontrada')
        return sale

    def product(pk):
        """Validador del campo product

        pk es un String
        """
        try:
            product = Product.objects.get(id=int(pk))
        except Product.DoesNotExist:
            raise serializers.ValidationError('1035: Producto no encontrado')
        return product
    
    def product_name(name):
        """Validador del campo product

        name es un String
        """
        try:
            product = Product.objects.get(name=name)
        except Product.DoesNotExist:
            raise serializers.ValidationError('1035: Producto no encontrado')
        return product

    def product_category(pk):
        """Validador del campo product_category

        pk es un String
        """
        try:
            product_category = ProductCategory.objects.get(id=int(pk))
        except ProductCategory.DoesNotExist:
            raise serializers.ValidationError('1036: Categoria del producto no encontrado')
        return product_category

    def recipe_category(pk):
        """Validador del campo recipe_category

        pk es un String
        """
        try:
            recipe_category = RecipeCategory.objects.get(id=int(pk))
        except RecipeCategory.DoesNotExist:
            raise serializers.ValidationError('1036: Categoria de la receta no encontrado')
        return recipe_category

    def recipe_category_name(name):
        """Validador del campo recipe_category

        name es un String
        """
        try:
            recipe_category = RecipeCategory.objects.get(name=name)
        except RecipeCategory.DoesNotExist:
            raise serializers.ValidationError('1036: Categoria de la receta no encontrado')
        return recipe_category

    def coupon(code):
        """Validador del campo coupon

        code es un String
        """
        try:
            coupon = Coupon.objects.get(code=int(code))
        except Coupon.DoesNotExist:
            raise serializers.ValidationError('1036: Cupon no encontrada')
        return coupon

    def user(username):
        """Validador del campo user

        username es un String
        """
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('1036: Usuario no encontrado')
        return user

    def recipe(pk):
        """Validador del campo recipe

        pk es un String
        """
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise serializers.ValidationError('1036: Receta no encontrado')
        return recipe
