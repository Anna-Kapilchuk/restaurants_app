from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from restaurants_app.models import RestaurantRating, DishRating


class RestaurantRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantRating
        exclude = ['restaurant']


class DetailedRestaurantRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantRating
        fields = '__all__'


class DishRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = DishRating
        exclude = ['dish']


class DetailedDishRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishRating
        fields = '__all__'
