from django.db import models


class Restaurant(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    address = models.CharField(null=False, blank=False, max_length=128)

    class Meta:
        db_table = 'restaurants'


class RestaurantDish(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    description = models.CharField(null=True, blank=True, max_length=256)
    price = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'restaurant_dishes'




