from django.db import transaction

from ..constants import CrawlerName
from ...constants import CrawlerStatus
from ...models import Crawler
from ....queue.helpers import kafka_crawler_init


def get_crawler_handler(crawler_name):
    # circular import.. TODO refactor
    from ....crawler.repository import youtube

    CRAWLER_HANDLER_MAP = {
        CrawlerName.YOUTUBE: youtube.crawl
    }

    return CRAWLER_HANDLER_MAP.get(crawler_name)


def create_crawler(name, crawler, crawler_config, run_after_seconds) -> Crawler:
    return Crawler.objects.create(
        name=name,
        crawler=crawler,
        crawler_config=crawler_config,
        run_after_seconds=run_after_seconds,
        status=CrawlerStatus.STOPPED,
        is_enabled=False
    )


def start_crawler_via_name(name):
    kafka_crawler_init.send({'name': name})


def stop_crawler_via_name(name):
    with transaction.atomic():
        crawler = Crawler.objects.filter(
            name=name,
            is_enabled=True,
            status=CrawlerStatus.RUNNING
        ).select_for_update().last()

        if not crawler:
            return

        crawler.is_enabled = False
        crawler.status = CrawlerStatus.STOPPED
        crawler.save()

    return crawler
