from rest_framework import serializers

from users.models import LmsUser

class LmsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsUser
        fields = "__all__"