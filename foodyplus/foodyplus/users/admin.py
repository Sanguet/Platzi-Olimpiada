# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from foodyplus.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """ Modelo custom del usuario admin"""

    list_display = ("email", "username", "is_staff", 'account_type')
    list_filter = ("is_staff", "created", "modified", 'account_type')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Perfil de admin"""

    list_display = ("user", 'picture', 'biografy')
    search_filter = ("user__username", "user__email")
    list_filter = ("points",)


admin.site.register(User, CustomUserAdmin)
