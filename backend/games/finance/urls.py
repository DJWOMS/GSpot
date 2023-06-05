from django.urls import path

from .views import OfferBundleAPIView, OfferInCartAPIView, ShowLibraryView

urlpatterns = [
    path('offer/', OfferBundleAPIView.as_view(), name="offer"),
    path("library/<user>", ShowLibraryView.as_view(), name="all_products_in_library"),
    path('offer-in-cart/', OfferInCartAPIView.as_view(), name="offer_in_cart")
]
