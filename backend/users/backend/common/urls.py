from django.urls import path

from common.views.v1.logout_view import JWTLogoutView

urlpatterns = [path('logout/', JWTLogoutView.as_view(), name="logout")]
