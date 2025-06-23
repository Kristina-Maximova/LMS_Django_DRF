from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    # добавить поле вывода количества уроков
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, instance):
        return instance.lessons.all().count()

    class Meta:
        model = Course
        fields = "__all__"
