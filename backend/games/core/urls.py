from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LinkDlcApiView, ProductViewSet, SystemRequirementViewSet


api_router = DefaultRouter()
api_router.register('product', ProductViewSet, basename='games')
api_router.register('system_requirement', SystemRequirementViewSet, basename='system_requirement')


urlpatterns = [
    path('', include(api_router.urls)),
    path('dlc/', LinkDlcApiView.as_view(), name='dlc-link'),
]
