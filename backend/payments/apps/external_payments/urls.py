from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    r'accept_payment',
    views.YookassaPaymentAcceptanceViewSet,
    basename='accept_payment',
)

urlpatterns = router.urls
