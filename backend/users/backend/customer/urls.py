from django.urls import path
from customer.views.v1.auth_view import CustomerAuthView
from customer.views.v1 import account_views
from customer.views.v1.customer_registration_view import CustomerRegistrationView


urlpatterns = [
    path("registration/", CustomerRegistrationView.as_view()),
]

account_router = [
    path(
        "customer/me",
        account_views.AccountViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"}
        ),
        name="customer-user-account",
    ),
    path(
        "customer/me/change-password",
        account_views.ChangePasswordViewSet.as_view({"post": "create"}),
        name="customer-user-change-password",
    ),
]

auth_routes = [path("login/", CustomerAuthView.as_view(), name="customer_login")]

urlpatterns += account_router
urlpatterns += auth_routes
