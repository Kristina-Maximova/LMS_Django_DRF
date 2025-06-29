from django.db import models

# from users.models import LmsUser - так ошибка с circular import
from config import settings

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    """Класс для представления курса"""

    title = models.CharField(max_length=200, verbose_name="Название курса")

    preview = models.ImageField(
        upload_to="course_images/",
        verbose_name="изображение",
        **NULLABLE,
        default="course_images/default_course.jpg",
        help_text="Загрузите изображение",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="пользователь",
    )
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, **NULLABLE)
    updated_at = models.DateTimeField(auto_now=True, **NULLABLE)

    def __str__(self):
        return f"Курс: {self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["-created_at"]


class Lesson(models.Model):
    """Класс для представления категории"""

    title = models.CharField(max_length=200, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    preview = models.ImageField(
        upload_to="lessons_images/",
        verbose_name="изображение",
        **NULLABLE,
        help_text="Загрузите изображение",
    )
    link = models.URLField(**NULLABLE)

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="lessons",
        verbose_name="курс",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="пользователь",
    )

    created_at = models.DateTimeField(auto_now_add=True, **NULLABLE)
    updated_at = models.DateTimeField(auto_now=True, **NULLABLE)

    def __str__(self):
        return f"Урок: {self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["-created_at"]
