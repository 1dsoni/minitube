from rest_framework import serializers

from .models import ApiKey


class ApiKeyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKey
        fields = '__all__'
