
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurants_app.views.address import AddressViewSet

router = DefaultRouter(trailing_slash=False)
router.register('', AddressViewSet)


urlpatterns = [

]

urlpatterns.extend(router.urls)
