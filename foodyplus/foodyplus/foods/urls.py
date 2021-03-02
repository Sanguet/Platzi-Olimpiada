# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Vistas
from .views import product_categories as product_categories_views
from .views import recipe_categories as recipe_categories_views
from .views import products as product_views
from .views import recipes as recipe_views
from .views import labels as label_views
from .views import recipe_labels as recipe_label_views
from .views import sales as sale_views
from .views import sale_details as sale_details_views
from .views import coupons as coupons_views
from .views import recipe_details as recipe_details_views
from .views import plannings as plannings_views
from .views import planning_details as plannings_details_views
from .views import recipe_comments as recipe_comments_views


router = DefaultRouter()
router.register(r'product_categories', product_categories_views.ProductCategoryViewSet, basename='product_category')
router.register(r'recipe_categories', recipe_categories_views.RecipeCategoryViewSet, basename='recipe_category')
router.register(r'products', product_views.ProductViewSet, basename='product')
router.register(r'recipes', recipe_views.RecipeViewSet, basename='recipes')
router.register(r'labels', label_views.LabelViewSet, basename='labels')
router.register(r'sales', sale_views.SaleViewSet, basename='sale')
router.register(r'coupons', coupons_views.CouponViewSet, basename='coupon')
router.register(r'plannings', plannings_views.PlanningViewSet, basename='planning')
router.register(
    r'recipes/(?P<recipe_pk>\d+)/labels',
    recipe_label_views.RecipeLabelViewSet,
    basename='recipe_label'
)
router.register(
    r'recipes/(?P<recipe_pk>\d+)/details',
    recipe_details_views.RecipeDetailViewSet,
    basename='recipe_detail'
)
router.register(
    r'recipes/(?P<recipe_pk>\d+)/comments',
    recipe_comments_views.RecipeCommentViewSet,
    basename='recipe_comment'
)
router.register(
    r'sales/(?P<sale_pk>\d+)/details',
    sale_details_views.SaleDetailViewSet,
    basename='sale_detail'
)
router.register(
    r'plannings/(?P<planning_pk>\d+)/details',
    plannings_details_views.PlanningDetailViewSet,
    basename='planning_detail'
)


urlpatterns = [
    path("", include(router.urls))
]
