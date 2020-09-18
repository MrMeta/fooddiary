from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('add', views.create_food, name='create_food'),
    path('<int:food_id>', views.food_detail, name='food_detail'),
    path('<int:food_id>/reviews/add', views.create_review, name='create_review'),
    path('store', views.store_list, name='store_list'),
    path('store/add', views.create_store, name='create_store'),
]