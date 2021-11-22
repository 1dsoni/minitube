import logging

from ..helpers import run_crawler_via_name
from ...commons.background import BackgroundTasks
from ...queue.helpers import kafka_crawler_init

logger = logging.getLogger(__name__)


def consume_crawler_events():
    kafka_crawler_init.consume(process_event)


def process_event(item):
    """
    item: {'name': name}
    """

    print('got %s', item)
    if not (item and 'name' in item):
        logger.warning('ignoring %s', item)
        return

    name = item['name']

    BackgroundTasks(target=run_crawler_via_name, kwargs={'name': name}).start()
