# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from foodyplus.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """ Modelo custom del usuario admin"""

    list_display = ("email", "username", "is_staff", "is_verified")
    list_filter = ("is_staff", "created", "modified")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Perfil de admin"""

    list_display = ("user", 'first_name', 'last_name', "points")
    search_filter = ("user__username", "user__email")
    list_filter = ("points",)


admin.site.register(User, CustomUserAdmin)