from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .viewsets import ApiKeyViewSet

router = SimpleRouter()
router.register('api-key', ApiKeyViewSet, 'api_key')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
