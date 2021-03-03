
# Django
from django.contrib import admin

# Models
from foodyplus.foods.models import (Coupon, Label, Planning, PlanningDetail, ProductCategory,
                                    Product, Recipe, RecipeCategory, RecipeDetail, RecipeComment,
                                    RecipeLabel, Sale, SaleDetail)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    """Coupon de admin"""

    list_display = ('user', 'name', 'code', 'discount', 'exp_date')
    search_filter = ('user', 'name', 'code', 'discount')
    list_filter = ('exp_date',)


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    """Label de admin"""

    list_display = ('name',)
    search_filter = ('name',)
    list_filter = ('name',)


@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):
    """Planning de admin"""

    list_display = ('user', 'name', 'format_date', 'description')
    search_filter = ('user', 'name', 'format_date', 'description')
    list_filter = ('user', 'format_date')


@admin.register(PlanningDetail)
class PlanningDetailAdmin(admin.ModelAdmin):
    """PlanningDetail de admin"""

    list_display = ('planning', 'recipe', 'day', 'time')
    search_filter = ('planning', 'recipe', 'day', 'time')
    list_filter = ('day', 'time')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product de admin"""

    list_display = ('product_category', 'name', 'cost', 'price', 'stock', 'provider', 'barcode',
                    'discount', 'description', 'picture', 'units_sales', 'unit')
    search_filter = ('product_category', 'name', 'provider')
    list_filter = ('product_category', 'provider')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """ProductCategory de admin"""

    list_display = ('name', 'usages', 'comment')
    search_filter = ('name',)
    list_filter = ('usages',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Recipe de admin"""

    list_display = ('recipe_category', 'name', 'picture',
                    'video', 'utensils', 'country', 'total_time', 'likes', 'portions')
    search_filter = ('recipe_category', 'name',
                     'country', 'total_time', 'likes', 'portions')
    list_filter = ('recipe_category', 'total_time', 'likes', 'portions')


@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    """RecipeCategory de admin"""

    list_display = ('name', 'comment')
    search_filter = ('name',)
    list_filter = ()


@admin.register(RecipeDetail)
class RecipeDetailAdmin(admin.ModelAdmin):
    """RecipeDetail de admin"""

    list_display = ('recipe', 'product', 'amount', 'unit', 'discount', 'sub_total')
    search_filter = ('recipe', 'product')
    list_filter = ()


@admin.register(RecipeComment)
class RecipeCommentAdmin(admin.ModelAdmin):
    """RecipeComment de admin"""

    list_display = ('recipe', 'user', 'comment')
    search_filter = ('recipe', 'user')
    list_filter = ()


@admin.register(RecipeLabel)
class RecipeLabelAdmin(admin.ModelAdmin):
    """RecipeLabel de admin"""

    list_display = ('recipe', 'label')
    search_filter = ('recipe', 'label')
    list_filter = ()


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    """Sale de admin"""

    list_display = ('user', 'shipping_info', 'discount', 'payment_method', 'total', 'delivery_charge',
                    'delivery_date', 'steps', 'comment', 'tracking_code', 'finalize')
    search_filter = ('user',  'tracking_code')
    list_filter = ('payment_method', 'delivery_date', 'steps', 'finalize')


@admin.register(SaleDetail)
class SaleDetailAdmin(admin.ModelAdmin):
    """SaleDetail de admin"""

    list_display = ('sale', 'product', 'amount', 'discount', 'sub_total')
    search_filter = ('sale')
    list_filter = ()
