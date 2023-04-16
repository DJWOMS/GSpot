from django.urls import path

from . import views

urlpatterns = [
    path('increase_balance/', views.BalanceIncreaseView.as_view()),
    path('payment_commission/', views.CalculatePaymentCommissionView.as_view()),
    path('accounts/users/', views.UserAccountAPIView.as_view(), name='user-accounts'),
    path('accounts/developers/', views.DeveloperAccountAPIView.as_view(), name='developer-accounts'),
    path('accounts/owners/', views.OwnerAccountAPIView.as_view(), name='owner-accounts'),
]
