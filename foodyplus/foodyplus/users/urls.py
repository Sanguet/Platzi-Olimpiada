# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Vistas
from .views import users as users_view
from .views import profiles as profiles_view
from .views import shipping_infos as shipping_info_view
from .views import favorites as favorites_views

router = DefaultRouter()
router.register(r"users", users_view.UserViewSet, basename="user")
router.register(r"profiles", profiles_view.ProfileViewSet, basename="profile")
router.register(r"shipping_infos", shipping_info_view.ShippingInfoViewSet, basename="shipping_info")
router.register(
    r'users/(?P<user_pk>\d+)/favorites',
    favorites_views.FavoriteViewSet,
    basename='favorite'
)

urlpatterns = [
    path("", include(router.urls))
]
