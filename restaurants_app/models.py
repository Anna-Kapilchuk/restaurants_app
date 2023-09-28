from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# class Address(models.Model):
#
#     city = models.CharField(max_length=128)
#     street = models.CharField(max_length=128)
#     h_number = models.SmallIntegerField(null=False, blank=False)
#
#     class Meta:
#         db_table = 'address'
#
#     def __str__(self):
#         return f"ID: {self.id}, city: {self.city}, street: {self.street}, number: {self.h_number}"


class Restaurant(models.Model):

    name = models.CharField(max_length=128)
    res_pic_url = models.URLField(max_length=512, db_column='pic_url', null=True, blank=True)
    res_type = models.CharField(max_length=128)
    phone_num = models.IntegerField(null=True, blank=True)
    instagram = models.URLField(max_length=512, null=True, blank=True)
    facebook = models.URLField(max_length=512, null=True, blank=True)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)

    user_rating = models.ManyToManyField(User, through='Visited')

    class Meta:
        db_table = 'restaurants'
        ordering = ['id']

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, address: {self.city} {self.street}"


class RestaurantDish(models.Model):

    name = models.CharField(max_length=128)
    description = models.CharField(null=True, blank=True, max_length=256)
    price = models.IntegerField(null=False, blank=False)
    dish_pic_url = models.URLField(max_length=512, db_column='pic_url', null=True, blank=True)
    dish_type = models.CharField(max_length=128, null=True, blank=True)

    restaurant = models.ForeignKey('Restaurant', on_delete=models.RESTRICT)
    user_rating = models.ManyToManyField(User, through='Tasted')

    class Meta:
        db_table = 'restaurant_dishes'
        ordering = ['id']

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"


class Visited(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    visited_v = models.BooleanField(default=True)

    rating_date = models.DateField(auto_now_add=True)
    restaurant_rating = models.SmallIntegerField(null=False, blank=False,
                                                 validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"restaurant: {self.restaurant.name}, user: {self.user.name}"

    class Meta:
        db_table = 'visited'


class Tasted(models.Model):
    dish = models.ForeignKey(RestaurantDish, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    tasted_v = models.BooleanField(default=True)

    rating_date = models.DateField(auto_now_add=True)
    dish_rating = models.SmallIntegerField(null=False, blank=False,
                                           validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"restaurant: {self.dish.name}, user: {self.user.name}"

    class Meta:
        db_table = 'tasted'


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.RESTRICT, related_name='profile')

    address = models.CharField(max_length=256, null=True)
    img_url = models.CharField(max_length=1024, null=True)

    class Meta:
        db_table = 'profiles'


# class RestaurantRating(models.Model):
#
#     rating = models.SmallIntegerField(null=False, blank=False,
#                                       validators=[MinValueValidator(1), MaxValueValidator(10)])
#     rating_date = models.DateField(auto_now_add=True)
#
#     created_by = models.ForeignKey(User, blank=True, on_delete=models.RESTRICT)
#     restaurant = models.ForeignKey('Restaurant', on_delete=models.RESTRICT)
#
#     class Meta:
#         db_table = 'restaurant_rating'
#         ordering = ['id']
#
#     def __str__(self):
#         return f"ID: {self.id}, Rating: {self.rating}, Date: {self.rating_date}, Restaurant: {self.restaurant}"


# class DishRating(models.Model):
#
#     rating = models.SmallIntegerField(null=False, blank=False,
#                                       validators=[MinValueValidator(1), MaxValueValidator(10)])
#     rating_date = models.DateField(auto_now_add=True)
#
#     created_by = models.ForeignKey(User, blank=True, on_delete=models.RESTRICT)
#     dish = models.ForeignKey('RestaurantDish', on_delete=models.RESTRICT)
#
#     class Meta:
#         db_table = 'dish_rating'
#         ordering = ['id']
#
#     def __str__(self):
#         return f"Rating: {self.rating}, Date: {self.rating_date}, Dish: {self.dish}"








