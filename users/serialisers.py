from rest_framework import serializers

from lms.serializers import CourseSerializer, LessonSerializer
from users.models import LmsUser, Payment


class LmsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsUser
        fields = ["id",
                  "password",
                  "is_superuser",
                  "is_staff", "is_active",
                  "date_joined",
                  "email",
                  "phone_number",
                  "avatar",
                  "city",
                  "username",
                  "groups",
                  "user_permissions", ]


class PaymentSerializer(serializers.ModelSerializer):
    user = LmsUserSerializer(read_only=True)
    course = CourseSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Payment
        fields = "__all__"
