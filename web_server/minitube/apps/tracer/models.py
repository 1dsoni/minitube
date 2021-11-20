from django.db import models

from ..commons.db.models import MyModel


class Trace(MyModel):
    entity = models.CharField(max_length=255)
    entity_id = models.CharField(max_length=255)

    request_trace = models.CharField(max_length=255)
    request_status = models.CharField(max_length=255)
    request_extra = models.JSONField(null=True, blank=True)
