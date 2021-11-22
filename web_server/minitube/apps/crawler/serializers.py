from rest_framework import serializers

from .models import Crawler


class CrawlerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crawler
        fields = ('id', 'name', 'crawler', 'crawler_config',
                  'run_after_seconds', 'status', 'is_enabled')


class CrawlerNameSerializer(serializers.Serializer):
    name = serializers.CharField()
