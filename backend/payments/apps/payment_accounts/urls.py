from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'payout_data', views.PayoutDataObjectViewSet)

urlpatterns = [
    path('increase_balance/', views.BalanceIncreaseView.as_view({'post': 'create'})),
    path('payment_commission/', views.CalculatePaymentCommissionView.as_view({'post': 'create'})),
    path('create_account/', views.UserCreateDeleteView.as_view({'post': 'create'})),
    path(
        'delete_account/<uuid:user_uuid>/',
        views.UserCreateDeleteView.as_view({'delete': 'destroy'}),
    ),
    path('balances/', views.BalanceViewSet.as_view({'post': 'list'})),
    path('balances/<uuid:user_uuid>/', views.BalanceViewSet.as_view({'get': 'retrieve'})),
    path('payout/', views.PayoutView.as_view({'post': 'create'})),
    path(
        'owner/',
        views.OwnerView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'}),
    ),
    path('payout_data/', views.PayoutDataCreateView.as_view({'post': 'create'})),
    path('payout_history/<uuid:user_uuid>/', views.PayoutHistoryView.as_view({'get': 'list'})),
    path(
        'refill_history/<uuid:user_uuid>/',
        views.RefillHistoryView.as_view({'get': 'list'}),
    ),
    path('', include(router.urls)),
]
