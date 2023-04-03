from django.urls import path

from . import views

urlpatterns = [
    path('accept_payment/', views.PaymentAcceptanceView.as_view()),
]
