from django.urls import path

from . import views

urlpatterns = [
    path('create_payment/', views.CreatePaymentView.as_view()),
    path('payment_acceptance/', views.CreatePaymentAcceptanceView.as_view()),
]
