from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

api_router = DefaultRouter()
api_router.register('games', views.GameViewSet, basename='games')

urlpatterns = [
    path('', include(api_router.urls)),
]
#     path('games/', views.GameViewSet, name="games"),
#
#     path('games/<str:name__iexact>/', views.GameViewSet.as_view({
#         "get": "retrieve", "delete": "retrieve", "patch": "update"
#     }), name="game"),
#
#     path('dlc/', views.DlcView.as_view({
#         "get": "list", "post": "create"
#     }), name="dlc-all"),
#     path('dlc/<int:pk>/', views.DlcView.as_view({
#         "get": "retrieve", "delete": "retrieve", "patch": "update"
#     }), name="dlc")
# ]
