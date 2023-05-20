from django.urls import path, include
from customer.views.v1 import account_views
from customer.views.v1.customer_registration_view import CustomerRegistrationView
from common import routes

account_router = [
    path(
        'customer/me',
        account_views.AccountViewSet.as_view(
            {'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'}
        ),
        name='customer-user-account',
    ),
    path(
        'customer/me/change-password',
        account_views.ChangePasswordViewSet.as_view({'post': 'create'}),
        name='customer-user-change-password',
    ),
]

urlpatterns = [path('registration/', CustomerRegistrationView.as_view())]

urlpatterns += account_router
