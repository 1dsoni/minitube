from django.conf import settings

from ..commons.api_helper import BaseApi


class EsApi(BaseApi):
    SERVICE_NAME = 'ELASTIC SEARCH'
    TIMEOUT = 2
    BASE_URL = settings.CONFIGS['ELASTIC_SEARCH']['BASE_URL']

    def search_youtube_vid_via_title(self, query):
        return self._post(
            'youtube_videos/_search?pretty=true&size=10',
            {
                "query": {
                    "bool": {
                        "minimum_should_match": 1,
                        "should": [
                            {
                                "multi_match": {
                                    "query": query,
                                    "type": "bool_prefix",
                                    "fields": [
                                        "title",
                                        "title._2gram",
                                        "title._3gram"
                                    ]
                                }
                            }
                        ]
                    }
                }
            }
        )


es_api = EsApi()
