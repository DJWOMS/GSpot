from django.urls import path

from . import views

urlpatterns = [
    path('increase_balance/', views.BalanceIncreaseView.as_view()),
    path('payment_commission/', views.CalculatePaymentCommissionView.as_view()),
    path('accounts/users/', views.UserAccountAPIView.as_view(), name='user-accounts'),
]
