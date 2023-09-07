from rest_framework import serializers

from restaurants_app.models import Restaurant, RestaurantDishes


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        #fields = '__all__'
        fields = ['id', 'name', 'address']
        #exclude = []
        #depth = 1

class DishesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantDishes
        fields = '__all__'


