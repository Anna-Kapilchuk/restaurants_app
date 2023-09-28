from rest_framework import serializers

from restaurants_app.models import Tasted


class DetailedTastedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasted
        fields = ['id', 'dish', 'user', 'tasted_v', 'dish_rating']

