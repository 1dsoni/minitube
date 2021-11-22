from rest_framework import mixins

from .models import ApiKey
from .serializers import ApiKeyModelSerializer
from ..commons.viewsets import BaseApiViewSet


class ApiKeyViewSet(BaseApiViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    serializer_class = ApiKeyModelSerializer
    queryset = ApiKey.objects.all()
