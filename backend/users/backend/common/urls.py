from django.urls import path, include
from rest_framework import routers

from common.views.v1.views import CountryViewSet, ContactTypeViewSet
from common.views.v1.logout_view import JWTLogoutView


router = routers.DefaultRouter()
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"contact_types", ContactTypeViewSet, basename="contact_type")

urlpatterns = [
    path("logout/", JWTLogoutView.as_view(), name="logout"),
    path("common/", include(router.urls)),
]
