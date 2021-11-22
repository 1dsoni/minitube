from rest_framework import serializers

from .models import Crawler, CrawledItem


class CrawlerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crawler
        fields = ('id', 'name', 'crawler', 'crawler_config',
                  'run_after_seconds', 'status', 'is_enabled')


class CrawlerNameSerializer(serializers.Serializer):
    name = serializers.CharField()


class CrawledItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawledItem
        fields = '__all__'


class CrawledItemIndexSerializer(serializers.Serializer):
    item_uid = serializers.CharField()
