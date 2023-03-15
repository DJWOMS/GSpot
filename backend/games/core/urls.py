from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

api_router = DefaultRouter()
api_router.register('games', views.GameViewSet, basename='games')
api_router.register('dlc', views.DlcViewSet, basename='dlc')
api_router.register('system_requirement', views.SystemRequirementViewSet, basename='system_requirement')
api_router.register('game_dlc', views.GameDlcLinkViewSet, basename='game_dlc')


urlpatterns = [
    path(r'v1/core/', include(api_router.urls)),
]
