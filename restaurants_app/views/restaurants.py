from django.db.models import Avg
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from restaurants_app.filterset.restaurants import RestaurantFilterSet
from restaurants_app.models import Restaurant
from restaurants_app.serializer.dishes import DishesSerializer
from restaurants_app.serializer.ratings import RestaurantRatingSerializer
from restaurants_app.serializer.restaurants import RestaurantSerializer, DetailedRestaurantSerializer, \
    CreateRestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    filterset_class = RestaurantFilterSet
    # permission_classes = [IsAuthenticated]

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

    def get_permissions(self):

        if self.action in ('create', 'update', 'destroy'):
            return [IsAdminUser()]

        else:
            return []  #no need permissions for GET (list, retrieve)

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return DetailedRestaurantSerializer

        elif self.action == 'create':
            return CreateRestaurantSerializer

        else:
            return super().get_serializer_class()