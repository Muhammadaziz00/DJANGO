from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import GeekUserChangeForm, GeekUserCreationForm
from users.models import GeekUser


class GeekUserAdmin(UserAdmin):
    add_form = GeekUserCreationForm
    form = GeekUserChangeForm
    models = GeekUser
    list_display = ("email", "is_staff", "is_acrive")
    list_editable = ("is_active")
    list_filter = ("email", "is_staff", "is_active")
    ordering = ("email", )
    search_fields = ("email",)
    fieldsets = (
        ("основная инфа", {"fields": ("email", "password")}),
        ("права доступа", {"fields": ("is_staff", "is_superuser", "is_active")}),
        ("Группы и огроничение", {"fields"; ( "groups", "user_permissions")}),
    )
    add_fieldsets=(
        ("создание пользователя",{
            "classes": ('wide'),
            "fields": ("email", "password1", "password2", "is_staff", "is_active", "groups", "user_permissions")}
        ),
    )


admin.site.register(GeekUser, GeekUserAdmin)