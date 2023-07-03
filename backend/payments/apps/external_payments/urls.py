from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'commissions', views.PaymentCommissionView, basename='commissions')
router.register(r'services', views.PaymentServiceView, basename='services')

urlpatterns = [
    path('accept_payment/', views.YookassaPaymentAcceptanceView.as_view({'post': 'create'})),
    path('', include(router.urls)),
]
