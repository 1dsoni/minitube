from rest_framework import mixins
from rest_framework.decorators import action

from .models import Crawler, CrawledItem
from .repository.crawled_item.helpers import get_crawled_item_via_item_uid
from .repository.crawler.helpers import (
    start_crawler_via_name, stop_crawler_via_name
)
from .serializers import CrawlerNameSerializer, CrawlerModelSerializer, \
    CrawledItemSerializer, CrawledItemIndexSerializer
from ..commons.responses import response_202, response_200
from ..commons.viewsets import BaseApiViewSet
from ..indexer.helpers import index_item
from ..indexer.worker.indexer import YOUTUBE_VID_ES_INDEX


class CrawlerViewSet(BaseApiViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin):
    serializer_class = CrawlerModelSerializer
    queryset = Crawler.objects.all()

    @action(methods=['POST'], detail=False, url_path='init')
    def init_crawler_view(self, request, *args, **kwargs):
        serializer = CrawlerNameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        start_crawler_via_name(name)
        return response_202({'name': name})

    @action(methods=['POST'], detail=False, url_path='stop')
    def stop_crawler_view(self, request, *args, **kwargs):
        serializer = CrawlerNameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        stop_crawler_via_name(name)
        return response_200({'name': name})


class CrawledItemViewSet(BaseApiViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    serializer_class = CrawledItemSerializer
    queryset = CrawledItem.objects.all()

    @action(methods=['POST'], detail=False, url_path='index')
    def index_crawled_item_view(self, request, *args, **kwargs):
        serializer = CrawledItemIndexSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item_uid = serializer.validated_data['item_uid']
        crawled_item = get_crawled_item_via_item_uid(item_uid)
        index_item(crawled_item.item, YOUTUBE_VID_ES_INDEX)

        return response_202({'name': item_uid})
