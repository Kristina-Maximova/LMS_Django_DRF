from django.core.management.base import BaseCommand

from users.models import LmsUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = LmsUser.objects.create(email="lmsadmin@example.com")
        user.set_password("123456La")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created admin user with email {user.email}"
            )
        )
