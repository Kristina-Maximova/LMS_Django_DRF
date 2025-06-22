from rest_framework import generics, permissions

from users.models import LmsUser, Payment
from users.serialisers import LmsUserSerializer, PaymentCreateSerializer


class LmsUserCreateAPIView(generics.CreateAPIView):
    serializer_class = LmsUserSerializer
    permissions = (permissions.IsAuthenticated,)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LmsUser

    def get_queryset(self):
        user = self.request.user
        return LmsUser.objects.filter(pk=user.pk)


class PaymentCreateAPIView(generics.CreateAPIView):
        serializer_class = PaymentCreateSerializer

