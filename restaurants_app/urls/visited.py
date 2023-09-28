
from rest_framework.routers import DefaultRouter
from restaurants_app.views.visited import VisitedViewSet

router = DefaultRouter(trailing_slash=False)
router.register('', VisitedViewSet)


urlpatterns = [

]

urlpatterns.extend(router.urls)
