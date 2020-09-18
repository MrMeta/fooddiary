from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('create', views.create_food, name='create_food'),
    path('store', views.store_list, name='store_list'),
]