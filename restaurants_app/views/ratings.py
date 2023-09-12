from rest_framework.viewsets import ModelViewSet

from restaurants_app.models import RestaurantRating, DishRating
from restaurants_app.serializer.ratings import DetailedRestaurantRatingSerializer, DishRatingSerializer


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
