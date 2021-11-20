from django.core.management import BaseCommand

from ...worker.indexer import consume_index_events


class Command(BaseCommand):

    def handle(self, *args, **options):
        consume_index_events()
