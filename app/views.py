from rest_framework import viewsets

from app.models import Store, Food, FoodReview
from app.serializers import StoreSerializer, FoodSerializer, FoodReviewSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodReviewViewSet(viewsets.ModelViewSet):
    queryset = FoodReview.objects.all()
    serializer_class = FoodReviewSerializer
