from django.urls import path, include
from rest_framework import routers

from common.views.v1.contenttype_view import ContactTypeViewSet
from common.views.v1.countrylist_view import CountryViewSet
from common.views.v1.logout_view import JWTLogoutView
from common.views.v1.get_jwt_view import GetJwtView

router = routers.DefaultRouter()
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"contact_types", ContactTypeViewSet, basename="contact_type")

urlpatterns = [
    path("logout/", JWTLogoutView.as_view(), name="logout"),
    path("get-jwt/", GetJwtView.as_view(), name="get-jwt"),
    path("common/", include(router.urls)),
]
