from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentListAPIView, PaymentUpdateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)

app_name = UsersConfig.name

urlpatterns = [
    # авторизация
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    # payments
    path("payments/", PaymentListAPIView.as_view(), name="payments"),
    path(
        "payments/<int:pk>/update",
        PaymentUpdateAPIView.as_view(),
        name="payments_update",
    ),
]
