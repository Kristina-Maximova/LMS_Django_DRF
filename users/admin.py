from django.contrib import admin

from .models import LmsUser


@admin.register(LmsUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
    )
    search_fields = ("email",)
