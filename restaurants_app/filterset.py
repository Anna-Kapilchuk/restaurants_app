import django_filters
from django_filters import FilterSet

from restaurants_app.models import *


class RestaurantFilterSet(FilterSet):

    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')
    res_type = django_filters.CharFilter(field_name='res_type', lookup_expr='iexact')

    class Meta:
        model = Restaurant
        fields = ['name', 'res_type']


class DishFilterSet(FilterSet):

    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')
    dish_type = django_filters.CharFilter(field_name='dish_type', lookup_expr='iexact')
    price_from = django_filters.NumberFilter('price', lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte')


class AddressFilterSet(FilterSet):

    city = django_filters.CharFilter(field_name='city', lookup_expr='iexact')
    street = django_filters.CharFilter(field_name='street', lookup_expr='iexact')




