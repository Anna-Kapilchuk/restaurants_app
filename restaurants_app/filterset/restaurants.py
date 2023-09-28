import django_filters
from django_filters.rest_framework import FilterSet

from restaurants_app.models import Restaurant


class RestaurantFilterSet(FilterSet):

    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')
    res_type = django_filters.CharFilter(field_name='res_type', lookup_expr='iexact')


    class Meta:
        model = Restaurant
        fields = []
