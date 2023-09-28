import django_filters
from django_filters.rest_framework import FilterSet

from restaurants_app.models import Visited


class ResRatingFilterSet(FilterSet):

    restaurant = django_filters.NumberFilter(field_name='restaurant', lookup_expr='exact')
    user = django_filters.NumberFilter(field_name='user', lookup_expr='exact')

    class Meta:
        model = Visited
        fields = []
