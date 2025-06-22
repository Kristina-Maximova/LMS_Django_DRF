from django.core.management import call_command
from django.core.management.base import BaseCommand

from lms.models import Course, Lesson
from users.models import LmsUser, Payment

class Command(BaseCommand):
    help = 'Adding data from fixtures'

    def handle(self, *args, **options):
        # Удаляем существующие записи:
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        LmsUser.objects.filter(is_superuser=False).delete()
        Payment.objects.all().delete()

        # Загружаем данные из фикстур
        call_command('loaddata', 'fixtures/course_fixture.json')
        call_command('loaddata', 'fixtures/lessons_fixture.json')
        call_command('loaddata', 'fixtures/users_fixture.json')
        call_command('loaddata', 'fixtures/payment_fixture.json')

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
