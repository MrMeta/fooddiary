from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    deleted_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True
