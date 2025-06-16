from django.contrib import admin

from lms.models import Course, Lesson


class ShortDescriptionMixin:
    ''' Миксин для сокращения поля 'description' в панели администратора '''

    def short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description


@admin.register(Course)
class CourseAdmin(ShortDescriptionMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'short_description']
    list_filter = []
    search_fields = ('name',)


@admin.register(Lesson)
class LessonAdmin(ShortDescriptionMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'short_description']
    list_filter = []
    search_fields = ('name',)
