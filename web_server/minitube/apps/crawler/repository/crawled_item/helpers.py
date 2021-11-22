import logging

from django.db import transaction

from ...constants import CrawledItemStatus
from ....crawler.models import CrawledItem, Crawler
from ....queue.helpers import kafka_indexer

logger = logging.getLogger(__name__)


def mark_queued_for_index(crawled_item: CrawledItem) -> CrawledItem:
    crawled_item.status = CrawledItemStatus.QUEUED_FOR_INDEX
    crawled_item.save()
    return crawled_item


def mark_item_indexed(crawled_item: CrawledItem) -> CrawledItem:
    crawled_item.status = CrawledItemStatus.INDEXED
    crawled_item.save()
    return crawled_item


def mark_item_failed_indexed(crawled_item: CrawledItem,
                             reason: str) -> CrawledItem:
    crawled_item.status = CrawledItemStatus.FAILED_TO_INDEX
    crawled_item.status_reason = reason or ''
    crawled_item.save()
    return crawled_item


def send_to_index_queue(crawled_item: CrawledItem):
    with transaction.atomic():
        crawled_item = mark_queued_for_index(crawled_item)

    transaction.on_commit(
        lambda: kafka_indexer.send({'item_uid': crawled_item.item_uid})
    )


def save_crawled_item(crawler: Crawler, item_uid, item):
    try:
        with transaction.atomic():
            out = CrawledItem.objects.create(
                crawler=crawler,
                item_uid=item_uid,
                item=item,
                status=CrawledItemStatus.INITIAL_SAVED
            )
            logger.error('%s: saved: %s', crawler.name, out.item_uid)
        transaction.on_commit(lambda: send_to_index_queue(out))
    except Exception as e:
        logger.exception('failed save_crawled_item, err: %s', str(e))


def get_queued_crawled_item_via_item_uid(item_uid) -> CrawledItem:
    return CrawledItem.objects.filter(
        item_uid=item_uid,
        status=CrawledItemStatus.QUEUED_FOR_INDEX
    ).first()


def get_crawled_item_via_item_uid(item_uid) -> CrawledItem:
    return CrawledItem.objects.filter(
        item_uid=item_uid,
    ).first()
