from django.core.management import BaseCommand

from ...worker.youtube import consume_crawler_events


class Command(BaseCommand):

    def handle(self, *args, **options):
        consume_crawler_events()
