from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from restaurants_app.filterset.visited import ResRatingFilterSet
from restaurants_app.models import Visited
from restaurants_app.serializer.visited import DetailedVisitedSerializer


class VisitedViewSet(ModelViewSet):

    serializer_class = DetailedVisitedSerializer
    queryset = Visited.objects.all()
    filterset_class = ResRatingFilterSet
    permission_classes = [IsAuthenticatedOrReadOnly]


