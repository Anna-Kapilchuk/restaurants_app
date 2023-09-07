

from django.contrib import admin
from django.urls import path, include
from restaurants_app import views


urlpatterns = [
    path('restaurants', views.get_restaurants),
    path('dish', views.get_dishes),

]
