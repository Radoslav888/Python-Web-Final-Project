from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from Hestia.accounts.forms import UserEditForm, UserCreateForm


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": (
            "first_name",
            "last_name",
            "email",
            "phone_number"
        )}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    form = UserEditForm
    add_form = UserCreateForm
