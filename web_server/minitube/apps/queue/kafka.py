import json
import logging

from kafka import KafkaProducer, KafkaConsumer

logger = logging.getLogger(__name__)


class KafkaQueueImplementation:
    def __init__(self, topic, brokers, group_id=None):
        self.topic = topic
        self.brokers = brokers
        self.group_id = group_id

        self._PRODUCER = None
        self._CONSUMER = None

    @property
    def producer(self):
        if not self._PRODUCER:
            self._PRODUCER = KafkaProducer(
                bootstrap_servers=self.brokers
            )
        return self._PRODUCER

    @property
    def consumer(self):
        if not self._CONSUMER:
            self._CONSUMER = KafkaConsumer(
                self.topic,
                bootstrap_servers=self.brokers,
                group_id=self.group_id,
                enable_auto_commit=True,
                auto_offset_reset='earliest',
                max_poll_interval_ms=12000,
                max_poll_records=1
            )
        return self._CONSUMER

    def send(self, data):
        data = json.dumps(data).encode('utf-8')
        return self.producer.send(topic=self.topic, value=data)

    def consume(self, processor_func):
        logger.info('%s Begin consume', self.topic)
        for message in self.consumer:
            try:
                message_value = json.loads(message.value)
            except:
                message_value = message.value

            try:
                processor_func(message_value)
            except Exception as e:
                logger.exception(
                    'Failed processing message, err: %s', str(e)
                )
                raise e

        logger.info('%s Stop consume', self.topic)
