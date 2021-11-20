from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])


def index_item(item, es_index):
    helpers.bulk(
        es,
        [{
            "_index": es_index,
            "_source": item,
        }],
        refresh='wait_for'
    )
