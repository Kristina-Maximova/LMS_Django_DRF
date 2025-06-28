from django.contrib import admin

from .models import LmsUser, Payment


@admin.register(LmsUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "phone_number",
        "city"
    )
    search_fields = ("email",)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "course", "lesson", "amount", "method",)
    list_filter = ["user", "date"]
    search_fields = ["user",  "date", "method"]