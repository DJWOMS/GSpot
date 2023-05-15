from django.urls import path

from .views import OfferAPIView


urlpatterns = [
    path('offer/', OfferAPIView.as_view(), name="offer"),
]
