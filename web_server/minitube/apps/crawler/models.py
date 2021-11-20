from django.db import models

from ..commons.db.models import MyModel


class Crawler(MyModel):
    name = models.CharField(max_length=255, unique=True)

    crawler = models.CharField(max_length=255, db_index=True)
    crawler_config = models.JSONField(null=True, blank=True)

    run_after_seconds = models.PositiveIntegerField()
    status = models.CharField(max_length=255, db_index=True)

    is_enabled = models.BooleanField()


class CrawledItem(MyModel):
    crawler = models.ForeignKey(Crawler, on_delete=models.PROTECT)
    item_uid = models.CharField(max_length=255, unique=True)
    item = models.JSONField()
    status = models.CharField(max_length=255)
    status_reason = models.TextField(blank=True)
