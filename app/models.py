from django.db import models
from django.utils import timezone


class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    # add longitude, latitude

    def __str__(self):
        return self.name


class Food(models.Model):
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
