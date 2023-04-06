from django.urls import path, include

from rest_framework.routers import DefaultRouter

from utils.views import (
    GetOperatingSystemViewSet,
    GetMinMaxPriceViewSet,
    GetGenreViewSet,
    GetSubGenreViewSet,
)


api_router = DefaultRouter()
api_router.register("filters/genres", GetGenreViewSet, basename="all_genres")
api_router.register("filters/sub_genres", GetSubGenreViewSet, basename="all_sub_genres")
api_router.register(
    "filters/platforms", GetOperatingSystemViewSet, basename="get_all_platforms"
)
api_router.register(
    "filters/prices", GetMinMaxPriceViewSet, basename="get_min_max_price"
)

urlpatterns = [
    path("", include(api_router.urls)),
]
