from django.urls import include, path
from rest_framework import routers

from . import views

offer_router = routers.SimpleRouter()
offer_router.register(r'update_offer', views.ItemPurchaseUpdaterViewSet, basename='update_offer')


urlpatterns = [
    path('purchase/', views.PurchaseItemView.as_view({'post': 'create'})),
    path('', include(offer_router.urls)),
]
