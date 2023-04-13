from django.urls import path

from . import views

urlpatterns = [
    path('increase_balance/', views.BalanceIncreaseView.as_view()),
    path('payment_commission/', views.CalculatePaymentCommissionView.as_view()),
    path('account/owner/<uuid:user_uuid>/', views.AccountOwnerAPIView.as_view(), name='account-owner'),
]

