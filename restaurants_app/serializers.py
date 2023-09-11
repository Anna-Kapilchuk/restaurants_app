from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from restaurants_app.models import *


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'res_type', 'res_pic_url']
        depth = 1


class DetailedRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'
        depth = 1


class CreateRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'
        # extra_kwargs = {
        #     'id': {'read_only': True}
        # }


class DishesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantDish
        exclude = ['restaurant']


class DetailedDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantDish
        fields = '__all__'


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


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class SignupSerializer(ModelSerializer):

    password = serializers.CharField(max_length=128, validators=[validate_password], write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'email': {'required': True},
            'username': {'read_only': True}
        }
        validators = [UniqueTogetherValidator(User.objects.all(), ['email'])]

    def create(self, validated_data):

        user = User.objects.create(username=validated_data['email'],
                                   email=validated_data['email'],
                                   first_name=validated_data.get('first_name', ''),
                                   last_name=validated_data.get('last_name', ''))
        user.set_password(validated_data['password'])
        user.save()
        return user




