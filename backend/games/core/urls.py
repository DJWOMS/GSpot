from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GameViewSet, DlcViewSet, SystemRequirementViewSet

api_router = DefaultRouter()
api_router.register('games', GameViewSet, basename='games')
api_router.register('dlc', DlcViewSet, basename='dlc')
api_router.register('system_requirement', SystemRequirementViewSet, basename='system_requirement')

urlpatterns = [
    path('v1/', include(api_router.urls)),
]
