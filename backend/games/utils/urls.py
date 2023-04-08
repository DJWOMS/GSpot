from django.urls import path

from utils.views import (
    GetOperatingSystemListView,
    GetGenreListView,
    GetMinMaxPriceListView,
)


urlpatterns = [
    path("filters/genres", GetGenreListView.as_view(), name="all_genres"),
    path(
        "filters/platforms", GetOperatingSystemListView.as_view(), name="all_platforms"
    ),
    path("filters/prices", GetMinMaxPriceListView.as_view(), name="min_max_price"),
]
