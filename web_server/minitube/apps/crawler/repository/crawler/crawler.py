import time

from .helpers import get_crawler_handler, mark_crawler_running, \
    mark_crawler_stopped
from ..crawled_item.helpers import save_crawled_item
from ....commons.utils import get_random_key
from ....crawler.models import Crawler


class CrawlerEntity(object):
    def __init__(self, crawler: Crawler):
        self.crawler = crawler

    def run(self):
        crawler_handler = get_crawler_handler(self.crawler.crawler)
        if callable(crawler_handler):
            mark_crawler_running(self.crawler)

            while self.can_crawl():
                crawler_handler(self)

            mark_crawler_stopped(self.crawler)

    def crawl_wait(self):
        run_after_seconds = self.crawler.run_after_seconds
        time.sleep(run_after_seconds)

    def can_crawl(self) -> bool:
        self.crawler.refresh_from_db()
        return self.crawler.is_enabled

    def get_config(self):
        return self.crawler.crawler_config

    def save_crawled_item(self, item):
        save_crawled_item(
            crawler=self.crawler,
            item_uid=get_random_key(),
            item=item
        )
