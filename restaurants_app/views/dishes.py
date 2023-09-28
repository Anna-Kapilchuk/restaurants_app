from django.db.models import Avg
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from restaurants_app.filterset.dishes import DishFilterSet
from restaurants_app.models import RestaurantDish
from restaurants_app.restaurant_permission import RestaurantPermission
from restaurants_app.serializer.dishes import DetailedDishSerializer


class DishViewSet(ModelViewSet):
    serializer_class = DetailedDishSerializer
    queryset = RestaurantDish.objects.all()
    filterset_class = DishFilterSet
    permission_classes = [RestaurantPermission]

    @action(detail=True, url_path='avg-rating')
    def avg_rating(self, request, pk=None):

        dish = self.get_object()
        avg = dish.tasted_set.aggregate(Avg('dish_rating'))

        return Response(avg)
