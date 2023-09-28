import django_filters
from django_filters.rest_framework import FilterSet

from restaurants_app.models import Tasted


class DishRatingFilterSet(FilterSet):

    dish = django_filters.NumberFilter(field_name='dish', lookup_expr='exact')
    user = django_filters.NumberFilter(field_name='user', lookup_expr='exact')

    class Meta:
        model = Tasted
        fields = []
