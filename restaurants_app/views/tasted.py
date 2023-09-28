from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from restaurants_app.filterset.tasted import DishRatingFilterSet
from restaurants_app.models import Tasted
from restaurants_app.serializer.tasted import DetailedTastedSerializer


class TastedViewSet(ModelViewSet):

    serializer_class = DetailedTastedSerializer
    queryset = Tasted.objects.all()
    filterset_class = DishRatingFilterSet
    permission_classes = [IsAuthenticatedOrReadOnly]
    # filterset_class =


