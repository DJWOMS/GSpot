from django.urls import path

from . import views

urlpatterns = [
    path('accept_payment/', views.YookassaPaymentAcceptanceViewSet.as_view({'post': 'create'})),
]
