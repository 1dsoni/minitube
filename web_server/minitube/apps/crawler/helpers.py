import logging

from .repository.crawler.crawler import CrawlerEntity
from .repository.crawler.helpers import get_stopped_crawler_via_name

logger = logging.getLogger(__name__)


def run_crawler_via_name(name):
    crawler = get_stopped_crawler_via_name(name)
    if not crawler:
        logger.warning('crawler %s not found', name)
        return

    ce = CrawlerEntity(crawler)
    ce.run()
