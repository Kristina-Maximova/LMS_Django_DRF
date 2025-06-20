from rest_framework import serializers

from users.models import LmsUser, Payment

class LmsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsUser
        fields = "__all__"

class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
