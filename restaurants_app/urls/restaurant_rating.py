from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurants_app.views.ratings import DishRatingViewSet, RestaurantRatingViewSet

router = DefaultRouter()
router.register('', RestaurantRatingViewSet)


urlpatterns = [

]

urlpatterns.extend(router.urls)
