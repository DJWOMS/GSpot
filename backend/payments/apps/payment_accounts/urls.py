from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    r'payment_commission',
    views.CalculatePaymentCommissionViewSet,
    basename='payment_commission',
)
router.register(r'increase_balance', views.BalanceIncreaseViewSet, basename='increase_balance')
router.register(r'create_account', views.UserAccountViewSet, basename='create_account')
router.register(r'user_balance/<uuid:user_uuid>', views.AccountBalanceViewSet, basename='user_balance')

urlpatterns = router.urls
