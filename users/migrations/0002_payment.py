# Generated by Django 5.2.3 on 2025-06-20 11:27

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0004_alter_course_created_at_alter_lesson_created_at"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateField(auto_now_add=True, null=True, verbose_name="дата"),
                ),
                (
                    "amount",
                    models.FloatField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0.001)],
                        verbose_name="сумма",
                    ),
                ),
                (
                    "methods",
                    models.CharField(
                        blank=True,
                        choices=[("cash", "наличные"), ("transfer", "перевод")],
                        max_length=8,
                        null=True,
                        verbose_name="способ оплаты",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment",
                        to="lms.course",
                        verbose_name="курс",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment",
                        to="lms.lesson",
                        verbose_name="урок ",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "платеж",
                "verbose_name_plural": "платежи",
                "ordering": ("-date",),
            },
        ),
    ]
