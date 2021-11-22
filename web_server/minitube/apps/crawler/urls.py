from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .viewsets import CrawlerViewSet

router = SimpleRouter()
router.register('crawler', CrawlerViewSet, 'crawler')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
