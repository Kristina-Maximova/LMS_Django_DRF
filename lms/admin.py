from django.contrib import admin

from lms.models import Course, Lesson


class ShortDescriptionMixin:
    """Миксин для сокращения поля 'description' в панели администратора"""

    def short_description(self, obj):
        if obj.description is None:
            return "(Нет описания)"
        return (
            obj.description[:50] + "..."
            if len(obj.description) > 50
            else obj.description
        )

    short_description.short_description = 'Краткое описание'

@admin.register(Course)
class CourseAdmin(ShortDescriptionMixin, admin.ModelAdmin):
    list_display = ["id", "title", "short_description"]
    list_filter = []
    search_fields = ("title",)


@admin.register(Lesson)
class LessonAdmin(ShortDescriptionMixin, admin.ModelAdmin):
    list_display = ["id", "title", "short_description"]
    list_filter = []
    search_fields = ("name",)
