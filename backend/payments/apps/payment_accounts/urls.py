from django.urls import path

from . import views

urlpatterns = [
    path('increase_balance/', views.BalanceIncreaseView.as_view()),
    path('payment_commission/', views.CalculatePaymentCommissionView.as_view()),
    path('create_account/', views.UserAccountAPIView.as_view()),
    path('balances/', views.BalanceViewSet.as_view({'post': 'list'})),
    path('balances/<uuid:user_uuid>/', views.BalanceViewSet.as_view({'get': 'retrieve'})),
    path('payout/', views.PayoutView.as_view({'post': 'create'})),
]
