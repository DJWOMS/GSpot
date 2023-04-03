from django.urls import path

from . import views

urlpatterns = [
    path('create_payment/', views.BalanceIncreaseView.as_view()),
    path('payment_commission/', views.CalculatePaymentCommissionView.as_view()),
]
