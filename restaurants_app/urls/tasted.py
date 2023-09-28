
from rest_framework.routers import DefaultRouter
from restaurants_app.views.tasted import TastedViewSet

router = DefaultRouter(trailing_slash=False)
router.register('', TastedViewSet)


urlpatterns = [

]

urlpatterns.extend(router.urls)
