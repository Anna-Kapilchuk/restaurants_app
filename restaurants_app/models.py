from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Address(models.Model):

    city = models.CharField(null=False, blank=False, max_length=128)
    street = models.CharField(null=False, blank=False, max_length=128)
    h_number = models.SmallIntegerField(null=False, blank=False)

    class Meta:
        db_table = 'address'

    def __str__(self):
        return f"ID: {self.id}, city: {self.city}, street: {self.street}, number: {self.h_number}"


class Restaurant(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    res_pic_url = models.URLField(max_length=512, db_column='pic_url', null=True, blank=True)
    res_type = models.CharField(null=False, blank=False, max_length=128)
    phone_num = models.IntegerField(null=True, blank=True)
    instagram_url = models.URLField(max_length=512, null=True, blank=True)
    facebook = models.URLField(max_length=512, null=True, blank=True)

    address = models.ForeignKey('Address', models.RESTRICT, null=True, blank=True)

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, address: {self.address}"


class RestaurantDish(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    description = models.CharField(null=True, blank=True, max_length=256)
    price = models.IntegerField(null=False, blank=False)         ### change to False
    dish_pic_url = models.URLField(max_length=512, db_column='pic_url', null=True, blank=True)
    dish_type = models.CharField(max_length=128, null=True, blank=True)

    restaurant = models.ForeignKey('Restaurant', models.RESTRICT, null=False, blank=False)

    class Meta:
        db_table = 'restaurant_dishes'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"


class RestaurantRating(models.Model):

    rating = models.SmallIntegerField(null=False, blank=False,
                                      validators=[MinValueValidator(1), MaxValueValidator(10)])
    rating_date = models.DateField(null=False, blank=False, auto_now_add=True)

    # created_by = models.ForeignKey(User)
    restaurant = models.ForeignKey('Restaurant', models.RESTRICT, null=False, blank=False)

    class Meta:
        db_table = 'restaurant_rating'

    def __str__(self):
        return f"ID: {self.id}, Rating: {self.rating}, Date: {self.rating_date}, Restaurant: {self.restaurant}"


class DishRating(models.Model):

    rating = models.SmallIntegerField(null=False, blank=False,
                                      validators=[MinValueValidator(1), MaxValueValidator(10)])
    rating_date = models.DateField(null=False, blank=False, auto_now_add=True)

    # created_by = models.ForeignKey(User)
    dish = models.ForeignKey('RestaurantDish', models.RESTRICT, null=False, blank=filter)

    class Meta:
        db_table = 'dish_rating'

    def __str__(self):
        return f"Rating: {self.rating}, Date: {self.rating_date}, Dish: {self.dish}"




