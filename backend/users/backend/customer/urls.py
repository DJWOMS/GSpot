from django.urls import path, include
from customer.views.v1 import account_views

from common import routes

router = routes.CustomChangeInfoAccountRouter()
router.register(r'customer/me', account_views.CustomerAccountViewSet, basename='customer-user-account')
change_pass_router = routes.CustomChangePasswordRouter()
change_pass_router.register(
    r'customer/me/change-password',
    account_views.CustomerChangePasswordViewSet,
    basename='customer-users-change-password'
)
urlpatterns = [
    path('users/', include(change_pass_router.urls)),
    path('users/', include(router.urls)),
]