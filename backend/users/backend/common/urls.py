from django.urls import path
from common.views.v1.logout_view import JWTLogoutView
from common.views.v1.get_jwt_view import GetJwtView

urlpatterns = [
    path('logout/', JWTLogoutView.as_view(), name="logout"),
    path('get-jwt/', GetJwtView.as_view(), name='get-jwt'),
]
