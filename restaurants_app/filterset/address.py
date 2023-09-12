import django_filters
from django_filters.rest_framework import FilterSet


class AddressFilterSet(FilterSet):

    city = django_filters.CharFilter(field_name='city', lookup_expr='iexact')
    street = django_filters.CharFilter(field_name='street', lookup_expr='iexact')
