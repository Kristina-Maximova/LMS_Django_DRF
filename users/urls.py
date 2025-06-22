from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentListAPIView, PaymentUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payments"),
    path(
        "payments/<int:pk>/update",
        PaymentUpdateAPIView.as_view(),
        name="payments_update",
    ),
]
