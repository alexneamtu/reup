from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Imports old documents to the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='+', type=int)

    # def handle(self, *args, **options):
        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Document.objects.get(pk=poll_id)
        #     except Document.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed document "%s"' % poll_id))