from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from restaurants_app.views.auth import signup, me

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/refresh', TokenRefreshView().as_view()),
    path('auth/signup', signup),
    path('auth/me', me),

]

