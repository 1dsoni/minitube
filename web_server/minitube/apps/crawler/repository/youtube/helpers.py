from collections import namedtuple

from ..constants import CrawlerName
from ..crawler.helpers import create_crawler
from ....api_key.repository.api_key.helpers import save_api_key, \
    fetch_new_active_key, mark_key_inactive

config = namedtuple('YouTubeConfig', ['query', 'max_results', 'api_key'])


def parse_config(crawler_config):
    query = crawler_config['query']
    api_key = crawler_config.get('api_key')
    max_results = crawler_config.get('max_results') or 25

    return config(query=query, max_results=max_results, api_key=api_key)


def create_youtube_crawler(name, query, max_results, run_after_seconds):
    return create_crawler(
        name=name,
        crawler=CrawlerName.YOUTUBE,
        crawler_config={
            'query': query,
            'max_results': max_results
        },
        run_after_seconds=run_after_seconds
    )


def save_youtube_api_key(key):
    return save_api_key(
        name='youtube_crawler_api_key',
        key=key,
        key_config=None
    )


def mark_old_key_inactive(api_key_obj):
    mark_key_inactive(
        name=api_key_obj.name,
        identifier=api_key_obj.identifier
    )


def get_new_youtube_api_key():
    # return 'AIzaSyBsWgDnzmg3zOJcm_g0DGORVvLMugUHYEI'
    api_key = fetch_new_active_key(name='youtube_crawler_api_key')
    if api_key:
        return api_key
    raise ValueError
