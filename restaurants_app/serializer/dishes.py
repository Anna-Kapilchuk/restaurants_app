from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from restaurants_app.models import RestaurantDish


class DishesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantDish
        exclude = ['restaurant']


class DetailedDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantDish
        fields = '__all__'
