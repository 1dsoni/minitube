import time

from .repository.crawler.helpers import get_all_enabled_crawlers


def start_crawlers():
    while True:
        time.sleep(5)
        crawlers = get_all_enabled_crawlers()
        if not crawlers:
            continue
