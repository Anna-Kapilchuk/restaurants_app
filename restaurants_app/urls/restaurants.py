
from rest_framework.routers import DefaultRouter
from restaurants_app.views.restaurants import RestaurantViewSet

router = DefaultRouter(trailing_slash=False)
router.register('', RestaurantViewSet)


urlpatterns = [

]

urlpatterns.extend(router.urls)
