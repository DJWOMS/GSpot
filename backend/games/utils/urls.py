from django.urls import path, include

from rest_framework.routers import DefaultRouter

from utils.views import (
    GetOperatingSystemListView,
    GetMinMaxPriceApiView,
    GetGenreViewSet,
    GetSubGenreViewSet,
)


api_router = DefaultRouter()
api_router.register("filters/genres", GetGenreViewSet, basename="all_genres")
api_router.register("filters/sub_genres", GetSubGenreViewSet, basename="all_sub_genres")

urlpatterns = [
    path("", include(api_router.urls)),
    path("filters/platforms", GetOperatingSystemListView.as_view(), name="get_all_platforms"),
    path("filters/prices", GetMinMaxPriceApiView.as_view(), name="get_min_max_price"),
]
