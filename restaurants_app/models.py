from django.db import models


class Restaurant(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    address = models.CharField(null=False, blank=False, max_length=128)
    res_pic_url = models.URLField(max_length=512, db_column='pic_url', null=True)
    res_type = models.CharField(null=False, blank=False, max_length=128)

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, address: {self.address}"


class RestaurantDishes(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    description = models.CharField(null=True, blank=True, max_length=256)
    price = models.IntegerField(null=True, blank=True)
    dish_pic_url = models.URLField(max_length=512, db_column='pic_url', null=True)
    restaurant = models.ForeignKey('Restaurant', models.RESTRICT, null=False, blank=False)

    class Meta:
        db_table = 'restaurant_dishes'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"






