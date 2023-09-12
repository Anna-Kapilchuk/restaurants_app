import django_filters
from django_filters.rest_framework import FilterSet


class DishFilterSet(FilterSet):

    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')
    dish_type = django_filters.CharFilter(field_name='dish_type', lookup_expr='iexact')
    price_from = django_filters.NumberFilter('price', lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
