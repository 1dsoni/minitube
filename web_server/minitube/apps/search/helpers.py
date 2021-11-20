from rest_framework import status

from .es_api import es_api


def search_vid_via_title(query):
    data, status_code = es_api.search_youtube_vid_via_title(query)

    if not status.is_success(status_code):
        return []

    return [item['_source'] for item in data['hits']['hits']]
