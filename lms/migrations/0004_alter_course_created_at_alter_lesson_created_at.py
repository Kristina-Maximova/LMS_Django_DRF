# Generated by Django 5.2.3 on 2025-06-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0003_alter_lesson_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
