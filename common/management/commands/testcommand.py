from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(0, 10):
            print("테스트 배치 실행,", i)
