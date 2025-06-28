from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, )
from users.apps import UsersConfig
from users.views import (PaymentListAPIView,
                         PaymentUpdateAPIView,
                         LmsUserCreateAPIView,
                         LsmUserRetrieveApiView,
                         LmsUserDestroyApiView,
                         LmsUserUpdateAPIView, LmsUserListApiView)

app_name = UsersConfig.name

urlpatterns = [
    # users
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('register/', LmsUserCreateAPIView.as_view(), name='register'),
    path('<int:pk>/detail/', LsmUserRetrieveApiView.as_view(), name='user_detail'),
    path('<int:pk>/update/', LmsUserUpdateAPIView.as_view(), name='user_update'),
    path('<int:pk>/delete/', LmsUserDestroyApiView.as_view(), name='user_delete'),
    path('', LmsUserListApiView.as_view(), name='users_list'),

    # payments
    path("payments/", PaymentListAPIView.as_view(), name="payments"),
    path(
        "payments/<int:pk>/update/",
        PaymentUpdateAPIView.as_view(),
        name="payments_update",
    ),
]
