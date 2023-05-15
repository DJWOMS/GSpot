from django.urls import path

from customer.views.v1.customer_registration_view import CustomerRegistrationView

urlpatterns = [
    path(
        'registration/',
        CustomerRegistrationView.as_view(),
    ),
]
