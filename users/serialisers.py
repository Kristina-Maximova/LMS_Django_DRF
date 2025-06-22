from rest_framework import serializers

from lms.serializers import CourseSerializer, LessonSerializer
from users.models import LmsUser, Payment


class LmsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsUser
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    user = LmsUserSerializer(read_only=True)
    course = CourseSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Payment
        fields = "__all__"
