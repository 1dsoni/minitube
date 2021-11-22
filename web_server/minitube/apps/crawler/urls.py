from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .viewsets import CrawlerViewSet, CrawledItemViewSet

router = SimpleRouter()
router.register('crawler', CrawlerViewSet, 'crawler')
router.register('crawled-item', CrawledItemViewSet, 'crawled_item')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
