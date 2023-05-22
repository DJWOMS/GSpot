from django.urls import path
from .views import CartAPIView, OfferAPIView, ShowLibraryView


urlpatterns = [
    path('offer/', OfferAPIView.as_view(), name="offer"),
    path("library/<user>", ShowLibraryView.as_view(), name="all_products_in_library"),
    path('cart/', CartAPIView.as_view(), name="cart")
]
