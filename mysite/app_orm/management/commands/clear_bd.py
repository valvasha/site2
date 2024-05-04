from typing import Any
from django.core.management.base import BaseCommand
from ...models import AbcModel


class Command(BaseCommand):
    help = 'Отчищает базу данных'

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write('Clear ABC database')
        all_objects = AbcModel.objects.all()
        for obj in all_objects:
            obj.delete()
        all_objects = AbcModel.objects.all()
        self.stdout.write(f'ABC DB: {all_objects}')
        self.stdout.write('The database has been cleaned up')
