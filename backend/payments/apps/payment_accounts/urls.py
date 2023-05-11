from django.urls import path

from . import views

urlpatterns = [
    path('increase_balance/', views.BalanceIncreaseViewSet.as_view({'post': 'create'})),
    path(
        'payment_commission/',
        views.CalculatePaymentCommissionViewSet.as_view({'post': 'create'}),
    ),
    path('create_account/', views.AccountViewSet.as_view({'post': 'create'})),
    path(
        'user_balance/<uuid:user_uuid>/',
        views.AccountBalanceViewSet.as_view({'get': 'retrieve'}),
    ),
]
