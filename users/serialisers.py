from rest_framework.serializers import ModelSerializer

from lms.serializers import CourseSerializer, LessonSerializer
from users.models import LmsUser, Payment


class LmsUserSerializer(ModelSerializer):
    class Meta:
        model = LmsUser
        fields = ["id",
                  "password",
                  "is_superuser",
                  "is_staff",
                  "is_active",
                  "date_joined",
                  "email",
                  "phone_number",
                  "avatar",
                  "city",
                  "username",
                  "first_name",
                  "last_name",
                  "groups",
                  "user_permissions"]

class NarrowedUserSerializer(ModelSerializer):
    class Meta:
        model=LmsUser
        fields = ("id", "email", "avatar", "phone_number", "city",)



class PaymentSerializer(ModelSerializer):
    user = LmsUserSerializer(read_only=True)
    course = CourseSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Payment
        fields = "__all__"
