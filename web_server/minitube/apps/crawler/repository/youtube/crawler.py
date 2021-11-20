from django.utils import timezone
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .helpers import parse_config, get_new_youtube_api_key, \
    mark_old_key_inactive
from ..crawler.crawler import CrawlerEntity


def youtube_video_search(query, api_key, max_results=25, page_token=None):
    search_response = build(
        'youtube',
        'v3',
        developerKey=api_key
    ).search().list(
        q=query,
        type="video",
        order="date",
        part='id,snippet',
        maxResults=max_results,
        pageToken=page_token
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append(search_result)

    if 'nextPageToken' in search_response:
        return search_response["nextPageToken"], videos

    return None, videos


def grab_videos(crawler, api_key, query, max_results, page_token=None):
    if page_token == -1:
        page_token = None

    res = youtube_video_search(query=query,
                               api_key=api_key,
                               max_results=max_results,
                               page_token=page_token)

    page_token = res[0]
    videos = res[1]

    for vid in videos:
        crawler.save_crawled_item(
            item={
                'video_id': vid['id']['videoId'],
                'title': vid['snippet']['title'],
                'description': vid['snippet']['description'],
                'thumbnail': vid['snippet']['thumbnails']['default']['url'],
                'published_at': timezone.datetime.strptime(
                    vid['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'
                ).isoformat()
            }
        )

    return page_token


def _crawl(crawler, query, max_results, api_key_obj):

    page_token = -1
    api_key = api_key_obj.key

    while page_token is not None and crawler.can_crawl():
        if page_token == -1:
            page_token = None

        try:
            page_token = grab_videos(crawler=crawler,
                                     api_key=api_key,
                                     query=query,
                                     max_results=max_results,
                                     page_token=page_token)
        except HttpError as e:
            if e.status_code == 403:
                mark_old_key_inactive(api_key_obj)
                api_key_obj = get_new_youtube_api_key()
                api_key = api_key_obj.key
                if page_token is None:
                    page_token = -1

        else:
            crawler.crawl_wait()


def crawl(crawler: CrawlerEntity):
    crawler_config = parse_config(crawler.get_config())

    query = crawler_config.query
    max_results = crawler_config.max_results

    api_key_obj = get_new_youtube_api_key()

    while crawler.can_crawl():
        _crawl(crawler, query, max_results, api_key_obj)
