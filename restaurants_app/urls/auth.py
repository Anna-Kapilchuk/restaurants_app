
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from restaurants_app.views.auth import UsersViewSet, me, upload_profile_img, google_login

router = DefaultRouter()
router.register('', UsersViewSet)


urlpatterns = [
    path('refresh', TokenRefreshView.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('me', me),
    path('google-auth', google_login),
    path('profile/img', upload_profile_img),

]
urlpatterns.extend(router.urls)

