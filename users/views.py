from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter, SearchFilter

from users.models import LmsUser, Payment
from users.permissions import IsModerator, IsOwner
from users.serialisers import (
    LmsUserSerializer,
    NarrowedUserSerializer,
    PaymentSerializer,
)


class LmsUserCreateAPIView(generics.CreateAPIView):
    serializer_class = LmsUserSerializer
    queryset = LmsUser.objects.all()
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(
            user.password
        )  # в user.password пароль незахеширован, станет хэширован
        user.save()


class LmsUserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NarrowedUserSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return LmsUser.objects.filter(pk=user.pk)


class LmsUserDestroyApiView(generics.DestroyAPIView):
    serializer_class = LmsUserSerializer
    queryset = LmsUser.objects.all()
    permission_classes = [IsOwner]


class LmsUserListApiView(generics.ListAPIView):
    serializer_class = NarrowedUserSerializer
    queryset = LmsUser.objects.all()
    permission_classes = [IsModerator]


class LsmUserRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = NarrowedUserSerializer
    queryset = LmsUser.objects.all()
    permission_classes = []


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ("course", "lesson", "method")
    search_fields = ["method"]
    ordering_fields = ["date"]


class PaymentUpdateAPIView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
