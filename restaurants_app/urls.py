from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from restaurants_app import views
from restaurants_app.views import *

router = DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('dishes', DishViewSet)
router.register('restaurant-rating', RestaurantRatingViewSet)
router.register('dishes-rating', DishRatingViewSet)
router.register('address', AddressViewSet)
print(router.urls)

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/refresh', TokenRefreshView().as_view()),
    path('auth/signup', signup),

]

urlpatterns.extend(router.urls)
