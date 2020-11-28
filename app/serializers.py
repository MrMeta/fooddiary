from rest_framework import serializers

from app.models import Store, Food, FoodReview


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'


class BaseFoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ['id', 'name', 'description']


class FoodUpsertSerializer(BaseFoodSerializer):
    store_id = serializers.IntegerField(required=True)

    class Meta(BaseFoodSerializer.Meta):
        fields = BaseFoodSerializer.Meta.fields + ['store_id']


class FoodSerializer(BaseFoodSerializer):
    store = StoreSerializer()

    class Meta(BaseFoodSerializer.Meta):
        fields = BaseFoodSerializer.Meta.fields + ['store']


class FoodReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodReview
        fields = '__all__'
