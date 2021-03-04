# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from foodyplus.users.models import User, Favorite, ShippingInfo


class CustomUserAdmin(UserAdmin):
    """ Modelo custom del usuario admin"""

    list_display = ("email", "username", "is_staff", 'account_type')
    list_filter = ("is_staff", "created", "modified", 'account_type')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Perfil de admin"""

    list_display = ('user', 'recipe')
    search_filter = ('user', 'recipe')
    list_filter = ('created', 'modified')


@admin.register(ShippingInfo)
class ShippingInfoAdmin(admin.ModelAdmin):
    """Perfil de admin"""

    list_display = ('user', 'first_name', 'last_name', 'country',
                    'street_address', 'apartament', 'city', 'state', 'zip_code')
    search_filter = ('user', 'first_name', 'last_name', 'country',
                     'street_address', 'apartament', 'city', 'state', 'zip_code')
    list_filter = ('city', 'country', 'state')


admin.site.register(User, CustomUserAdmin)
