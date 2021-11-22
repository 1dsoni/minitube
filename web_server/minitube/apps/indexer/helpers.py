import logging

from django.conf import settings
from elasticsearch import Elasticsearch
from elasticsearch import helpers

logger = logging.getLogger(__name__)

es_host = settings.CONFIGS['ELASTIC_SEARCH']['BASE_URL']

es = Elasticsearch(hosts=[es_host])


def index_item(item, es_index):
    logger.info('indexing %s', item)
    helpers.bulk(
        es,
        [{
            "_index": es_index,
            "_source": item,
        }],
        refresh='wait_for'
    )
