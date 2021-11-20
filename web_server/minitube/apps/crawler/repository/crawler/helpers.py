from ..constants import CrawlerName
from ...constants import CrawlerStatus
from ...models import Crawler


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


def get_all_enabled_crawlers():
    return Crawler.objects.filter(
        is_enabled=True,
        status=CrawlerStatus.STOPPED
    )
