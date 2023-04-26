from django.urls import path
from rest_framework_simplejwt import views


urlpatterns = [
    path("auth/jwt/refresh/", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    path("auth/jwt/verify/", views.TokenVerifyView.as_view(), name="jwt-verify"),
]