from django.utils import timezone
from rest_framework import viewsets

from app.models import Store, Food, FoodReview
from app.serializers import StoreSerializer, FoodSerializer, FoodReviewSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.filter(deleted_date__isnull=True)
    serializer_class = StoreSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def perform_destroy(self, instance):
        instance.deleted_date = timezone.now()
        instance.save()


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodReviewViewSet(viewsets.ModelViewSet):
    queryset = FoodReview.objects.all()
    serializer_class = FoodReviewSerializer
