from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('create', views.create_food, name='create_food'),
    path('<int:id>', views.food_detail, name='food_detail'),
    path('store', views.store_list, name='store_list'),
    path('store/add', views.create_store, name='create_store'),
]