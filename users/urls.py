from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, )
from users.apps import UsersConfig
from users.views import (PaymentListAPIView,
                         PaymentUpdateAPIView,
                         LmsUserCreateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', LmsUserCreateAPIView.as_view(), name='register'),

    path("payments/", PaymentListAPIView.as_view(), name="payments"),
    path(
        "payments/<int:pk>/update/",
        PaymentUpdateAPIView.as_view(),
        name="payments_update",
    ),
]
