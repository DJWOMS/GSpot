from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LinkDlcApiView, ProductViewSet, SystemRequirementViewSet, SaveToLibraryAPIView


api_router = DefaultRouter()
api_router.register('product', ProductViewSet, basename='games')
api_router.register('system_requirement', SystemRequirementViewSet, basename='system_requirement')


urlpatterns = [
    path('', include(api_router.urls)),
    path('dlc/', LinkDlcApiView.as_view(), name='dlc-link'),
    path('save_to_library/', SaveToLibraryAPIView.as_view(), name='save_to_library'),

]
