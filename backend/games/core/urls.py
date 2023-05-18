from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LinkDlcApiView, ProductViewSet, SystemRequirementViewSet, save_to_library


api_router = DefaultRouter()
api_router.register('product', ProductViewSet, basename='games')
api_router.register('system_requirement', SystemRequirementViewSet, basename='system_requirement')
api_router.register('products', ProductViewSet, basename='products')


urlpatterns = [
    path('', include(api_router.urls)),
    path('dlc/', LinkDlcApiView.as_view(), name='dlc-link'),
    path('save_to_library', save_to_library, name='save_to_library'),
    path('recieve_gift', save_to_library, name='recieve_gift'),
]
