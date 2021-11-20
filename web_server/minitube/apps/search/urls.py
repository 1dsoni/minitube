from django.http import JsonResponse
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .viewsets import SearchVideoViewSet

router = SimpleRouter()
router.register('search', SearchVideoViewSet, 'search')

urlpatterns = [
    path('api/v1/search/ht', lambda x: JsonResponse({'status': 'ok'})),
    path('api/v1/', include(router.urls)),
]
