from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restaurants_app.models import *
from restaurants_app.serializers import RestaurantSerializer


@api_view(['GET'])
def get_restaurants(request):

    all_restaurants = Restaurant.objects.all()

    if 'name' in request.query_params:
        all_restaurants = all_restaurants.filter(name__iexact=request.query_params['name'])

    if 'res_type' in request.query_params:
        all_restaurants = all_restaurants.filter(res_type__iexact=request.query_params['res_type'])

    serializer = RestaurantSerializer(instance=all_restaurants, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def get_dishes(request):
    all_dishes = RestaurantDishes.objects.all()
    return Response()


