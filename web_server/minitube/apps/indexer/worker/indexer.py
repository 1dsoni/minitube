import logging

from django.conf import settings

from ..helpers import index_item
from ...crawler.repository.crawled_item.helpers import mark_item_failed_indexed, \
    mark_item_indexed, get_queued_crawled_item_via_item_uid
from ...queue.helpers import kafka_indexer

logger = logging.getLogger(__name__)
YOUTUBE_VID_ES_INDEX = settings.CONFIGS['ELASTIC_SEARCH']['INDEXES'][
    'YOUTUBE_VIDEO']


def consume_index_events():
    kafka_indexer.consume(process_event)


def process_event(item):
    """
    item: {'item_uid': item_uid}
    """
    logger.info('got item %s', item)
    if not (item and 'item_uid' in item):
        return

    item_uid = item['item_uid']

    crawled_item = get_queued_crawled_item_via_item_uid(item_uid)

    if not crawled_item:
        return

    try:
        index_item(crawled_item.item, YOUTUBE_VID_ES_INDEX)
    except Exception as e:
        mark_item_failed_indexed(crawled_item, str(e))
    else:
        mark_item_indexed(crawled_item)
