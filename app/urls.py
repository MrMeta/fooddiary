from django.urls import path, include
from rest_framework.routers import DefaultRouter
import views

router = DefaultRouter()
router.register(r'stores', views.StoreViewSet)
router.register(r'foods', views.FoodViewSet)
router.register(r'food-reviews', views.FoodReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]