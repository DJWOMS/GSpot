from django.urls import path, include
from rest_framework import routers

from .views.v1.views import CountryViewSet, ContactTypeViewSet

router = routers.DefaultRouter()
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"contact_types", ContactTypeViewSet, basename="contact_type")

urlpatterns = [
    path("api/v1/users/common/", include(router.urls)),
]
