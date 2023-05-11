from django.urls import path

from . import views

urlpatterns = [
    path('purchase/', views.PurchaseItemViewSet.as_view({'post': 'create'})),
]
