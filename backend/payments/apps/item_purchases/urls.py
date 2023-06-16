from django.urls import path

from . import views

urlpatterns = [
    path('purchase/', views.PurchaseItemView.as_view({'post': 'create'})),
    path('refund/', views.RefundView.as_view({'post': 'create'})),
    path(
        'item-purchase-history/<uuid:account_id>/',
        views.ItemPurchaseHistoryView.as_view({'get': 'list'}),
    ),
]
