from django.utils import timezone
from rest_framework import viewsets

from app.models import Store, Food, FoodReview
from app.serializers import StoreSerializer, FoodSerializer, FoodReviewSerializer, FoodUpsertSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.filter(deleted_date__isnull=True)
    serializer_class = StoreSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def perform_destroy(self, instance):
        instance.deleted_date = timezone.now()
        instance.save()


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(
        deleted_date__isnull=True,
        store__deleted_date__isnull=True,
    )
    http_method_names = ['get', 'post', 'patch', 'delete']

    def perform_destroy(self, instance):
        instance.deleted_date = timezone.now()
        instance.save()

    def get_serializer_class(self):
        if self.action in {'retrieve', 'list'}:
            return FoodSerializer
        return FoodUpsertSerializer


class FoodReviewViewSet(viewsets.ModelViewSet):
    queryset = FoodReview.objects.all()
    serializer_class = FoodReviewSerializer
