from django.urls import path

from . import views

urlpatterns = [
    path('purchase/', views.PurchaseItemView.as_view({'post': 'create'})),
]
