from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from restaurants_app.filterset import *
from restaurants_app.models import *
from restaurants_app.serializers import *


class RestaurantViewSet(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    filterset_class = RestaurantFilterSet

    @action(detail=True)
    def dishes(self, request, pk=None):

        restaurant = self.get_object()
        all_dishes = restaurant.restaurantdish_set.all()
        serializer = DishesSerializer(instance=all_dishes, many=True)

        return Response(data=serializer.data)

    @action(detail=True)
    def rating(self, request, pk=None):

        restaurant = self.get_object()
        all_ratings = restaurant.restaurantrating_set.all()
        serializer = RestaurantRatingSerializer(instance=all_ratings, many=True)

        return Response(data=serializer.data)

    @action(detail=True, url_path='rating/avg')
    def avg_rating(self, request, pk=None):

        restaurant = self.get_object()
        avg = restaurant.restaurantrating_set.aggregate(Avg('rating'))

        return Response(avg)

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return DetailedRestaurantSerializer

        elif self.action == 'create':
            return CreateRestaurantSerializer

        else:
            return super().get_serializer_class()


class DishViewSet(ModelViewSet):
    serializer_class = DetailedDishSerializer
    queryset = RestaurantDish.objects.all()
    filterset_class = DishFilterSet

    @action(detail=True)
    def rating(self, request, pk=None):

        dish = self.get_object()
        all_ratings = dish.dishrating_set.all()
        serializer = DishRatingSerializer(instance=all_ratings, many=True)

        return Response(data=serializer.data)

    @action(detail=True, url_path='rating/avg')
    def avg_rating(self, request, pk=None):

        dish = self.get_object()
        avg = dish.dishrating_set.aggregate(Avg('rating'))

        return Response(avg)

    # def get_serializer_class(self):
    #
    #     if self.action == 'GET':
    #         return DishRatingSerializer
    #
    #     else:
    #         return super().get_serializer_class()


class RestaurantRatingViewSet(ModelViewSet):

    serializer_class = DetailedRestaurantRatingSerializer
    queryset = RestaurantRating.objects.all()

    # def get_serializer_class(self):
    #
    #     if self.action == 'GET':
    #         return RestaurantRatingSerializer
    #
    #     else:
    #         return super().get_serializer_class()


class DishRatingViewSet(ModelViewSet):

    serializer_class = DishRatingSerializer
    queryset = DishRating.objects.all()

    # def get_serializer_class(self):
    #
    #     if self.action == 'GET':
    #         return DishRatingSerializer
    #
    #     else:
    #         return super().get_serializer_class()


class AddressViewSet(ModelViewSet):

    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    filterset_class = AddressFilterSet


@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(data=serializer.data)



#
# @api_view(['GET'])
# def get_avg_restaurant_rating(request, restaurant_id):
#
#     restaurant = get_object_or_404(Restaurant, id=restaurant_id)
#     avg_rating = restaurant.restaurantrating_set.aggregate(Avg('rating'))

