import csv
from pathlib import Path
from django.core.management.base import BaseCommand


from ...models import Document


class Command(BaseCommand):
    help = 'Imports old documents to the database from csv with the `id,md5,sha1` header.'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=Path, help='The csv to import.')

    def handle(self, *args, **options):
        imported = 0
        with open(options['csv_path']) as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    Document.objects.create(
                        old_id=row['id'],
                        md5=row['md5'],
                        sha1=row['sha1'],
                    )
                    imported += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(e))

            self.stdout.write(self.style.SUCCESS('Successfully imported "%d" documents.' % imported))
