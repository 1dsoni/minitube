from django.conf import settings

from ..queue.kafka import KafkaQueueImplementation

kafka_indexer = KafkaQueueImplementation(
    topic=settings.CONFIGS['KAFKA']['TOPICS']['SEARCH_INDEX'],
    brokers=settings.CONFIGS['KAFKA']['BROKERS']['SEARCH_INDEX'],
    group_id=settings.CONFIGS['KAFKA']['CONSUMERS']['SEARCH_INDEX']
)

kafka_crawler_init = KafkaQueueImplementation(
    topic=settings.CONFIGS['KAFKA']['TOPICS']['CRAWLER_INIT'],
    brokers=settings.CONFIGS['KAFKA']['BROKERS']['CRAWLER_INIT'],
    group_id=settings.CONFIGS['KAFKA']['CONSUMERS']['CRAWLER_INIT']
)
