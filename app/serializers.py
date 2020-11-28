from rest_framework import serializers

from app.models import Store, Food, FoodReview


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'


class FoodReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodReview
        fields = '__all__'
