from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from lms.models import Course, Lesson


class LmsUser(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите эл.почту"
    )
    phone_number = PhoneNumberField(
        region="RU",
        blank=True,
        null=True,
        verbose_name="Телефон",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите фото, по-желанию",
    )
    city = models.CharField(
        max_length=25,
        verbose_name="Город",
        help_text="Укажите Ваш город",
        blank=True,
        null=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    CASH = "cash"
    TRANSFER = "transfer"
    METHOD_CHOICES = [(CASH, "наличные"), (TRANSFER, "перевод")]

    user = models.ForeignKey(
        LmsUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="payment",
        verbose_name="пользователь",
    )
    date = models.DateField(
        auto_now_add=True, null=True, blank=True, verbose_name="дата"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="курс",
        related_name="payment",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="урок ",
        related_name="payment",
    )
    amount = models.FloatField(
        validators=[MinValueValidator(0.001)],
        null=True,
        blank=True,
        verbose_name="сумма",
    )
    method = models.CharField(
        max_length=8,
        choices=METHOD_CHOICES,
        verbose_name="способ оплаты",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.course if self.course else self.lesson} - {self.method} - {self.amount}"

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
        ordering = ("-date",)
