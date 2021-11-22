from rest_framework import mixins
from rest_framework.decorators import action

from .models import Crawler
from .repository.crawler.helpers import (
    start_crawler_via_name, stop_crawler_via_name
)
from .serializers import CrawlerNameSerializer, CrawlerModelSerializer
from ..commons.responses import response_202, response_200
from ..commons.viewsets import BaseApiViewSet


class CrawlerViewSet(BaseApiViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
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
