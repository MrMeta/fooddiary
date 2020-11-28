from rest_framework import serializers

from app.models import Store, Food, FoodReview


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'


class BaseFoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ['id', 'name', 'description', 'created_date', 'deleted_date']


class FoodUpsertSerializer(BaseFoodSerializer):
    store_id = serializers.IntegerField(required=True)

    class Meta(BaseFoodSerializer.Meta):
        fields = BaseFoodSerializer.Meta.fields + ['store_id']


class FoodSerializer(BaseFoodSerializer):
    store = StoreSerializer()

    class Meta(BaseFoodSerializer.Meta):
        fields = BaseFoodSerializer.Meta.fields + ['store']


class BaseFoodReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodReview
        fields = ['id', 'title', 'content', 'updated_date', 'created_date', 'deleted_date']


class FoodReviewUpsertSerializer(BaseFoodReviewSerializer):
    food_id = serializers.IntegerField(required=True)

    class Meta(BaseFoodReviewSerializer.Meta):
        fields = BaseFoodReviewSerializer.Meta.fields + ['food_id']


class FoodReviewSerializer(BaseFoodReviewSerializer):
    food = FoodSerializer()

    class Meta(BaseFoodReviewSerializer.Meta):
        fields = BaseFoodReviewSerializer.Meta.fields + ['food']
