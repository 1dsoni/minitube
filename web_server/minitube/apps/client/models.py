from django.db import models

from ..commons.db.models import MyModel


class Client(MyModel):
    name = models.CharField(max_length=255, db_index=True)
    identifier = models.CharField(max_length=255,
                                  unique=True)
    secret = models.CharField(max_length=255,
                              unique=True)

    status = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['identifier', 'secret'])
        ]
