from django.urls import path
from finance.views import OfferAPIView, ShowLibraryView


urlpatterns = [
    path('offer/', OfferAPIView.as_view(), name="offer"),
    path("library/<user>", ShowLibraryView.as_view(), name="all_products_in_library")
]
