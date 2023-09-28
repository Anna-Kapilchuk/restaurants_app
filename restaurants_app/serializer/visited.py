
from rest_framework import serializers

from restaurants_app.models import Visited


class DetailedVisitedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visited
        fields = ['id', 'restaurant_rating', "restaurant", 'user', 'visited_v']
