from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'payout_data', views.PayoutDataObjectViewSet)

urlpatterns = [
    path('increase_balance/', views.BalanceIncreaseView.as_view()),
    path('payment_commission/', views.CalculatePaymentCommissionView.as_view()),
    path('create_account/', views.UserAccountAPIView.as_view()),
    path('balances/', views.BalanceViewSet.as_view({'post': 'list'})),
    path('balances/<uuid:user_uuid>/', views.BalanceViewSet.as_view({'get': 'retrieve'})),
    path('payout/', views.PayoutView.as_view({'post': 'create'})),
    path('payout_data/', views.PayoutDataCreateView.as_view({'post': 'create'})),
    path('', include(router.urls)),
]
