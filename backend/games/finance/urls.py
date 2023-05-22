from django.urls import path

from .views import CartAPIView, OfferAPIView


urlpatterns = [
    path('offer/', OfferAPIView.as_view(), name="offer"),
    path('cart/', CartAPIView.as_view(), name="cart")
]
