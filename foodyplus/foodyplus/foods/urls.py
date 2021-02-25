# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Vistas
from .views import product_categories as product_categories_views
from .views import recipe_categories as recipe_categories_views
from .views import products as product_views


router = DefaultRouter()
router.register(r'product_categories', product_categories_views.ProductCategoryViewSet, basename='product_category')
router.register(r'recipe_categories', recipe_categories_views.RecipeCategoryViewSet, basename='recipe_category')
router.register(r'products', product_views.ProductViewSet, basename='product')


urlpatterns = [
    path("", include(router.urls))
]
