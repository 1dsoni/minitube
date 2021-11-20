from django.db import models


class CustomManager(models.Manager):

    def get_queryset(self):
        return super(CustomManager, self).get_queryset().filter(is_deleted=0)


class MyModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.IntegerField(default=0)

    objects = CustomManager()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self._meta.db_table}, id={self.pk}'
