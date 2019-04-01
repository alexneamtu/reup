import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import IntegrityError


from ...models import Document


class Command(BaseCommand):
    help = 'Imports old documents to the database from csv with the `id,md5,sha1` header.'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=Path, help='The csv to import.')

    def handle(self, *args, **options):
        imported = 0
        errors = 0
        with open(options['csv_path']) as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    _, created = Document.objects.get_or_create(
                        old_id=row['id'],
                        md5=row['md5'],
                        sha1=row['sha1'],
                    )
                    imported += 1
                except IntegrityError as e:
                    errors += 1
                    print(e)

            if errors:
                self.stdout.write(self.style.WARNING('Imported "%d" documents with "%d" errors' % (imported, errors)))
            else:
                self.stdout.write(self.style.SUCCESS('Successfully imported "%d" documents.' % imported))
