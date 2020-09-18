from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('/craete', views.create_food, name='create_food')
]