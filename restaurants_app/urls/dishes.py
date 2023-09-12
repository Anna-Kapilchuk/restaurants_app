
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurants_app.views.dishes import DishViewSet

router = DefaultRouter(trailing_slash=False)
router.register('', DishViewSet)


urlpatterns = [

]

urlpatterns.extend(router.urls)
