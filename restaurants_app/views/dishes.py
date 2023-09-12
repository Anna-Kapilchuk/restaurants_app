from django.db.models import Avg
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from restaurants_app.filterset.dishes import DishFilterSet
from restaurants_app.models import RestaurantDish
from restaurants_app.serializer.dishes import DetailedDishSerializer
from restaurants_app.serializer.ratings import DishRatingSerializer


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

    def get_permissions(self):

        if self.action in ('create', 'update', 'destroy'):
            return [IsAdminUser()]

        else:
            return []

    # def get_serializer_class(self):
    #
    #     if self.action == 'GET':
    #         return DishRatingSerializer
    #
    #     else:
    #         return super().get_serializer_class()
