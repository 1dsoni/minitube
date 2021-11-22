from django.db import models

from ..commons.db.models import MyModel


class ApiKey(MyModel):
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255, unique=True)
    key = models.TextField()
    key_config = models.JSONField(null=True, blank=True)
    is_active = models.BooleanField()
