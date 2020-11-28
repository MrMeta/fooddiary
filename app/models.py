from django.db import models

from fooddiary.models import BaseModel


class Store(BaseModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    # add longitude, latitude

    def __str__(self):
        return self.name


class Food(models.Model):
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class FoodReview(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s#%s' % (self.food, self.id)
