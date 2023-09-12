
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from restaurants_app.views.restaurants import RestaurantViewSet

router = DefaultRouter(trailing_slash=False)
router.register('', RestaurantViewSet)


urlpatterns = [

]

urlpatterns.extend(router.urls)
