from administrator.views.v1 import (
    AdminGroupViewSet,
    AdminPermissionViewSet,
    account_views,
)
from administrator.views.v1.auth_view import AdminAuthView
from administrator.views.v1.company_view import CompanyListView
from administrator.views.v1.customer_view import CustomerListView
from administrator.views.v1.developer_view import DeveloperListView
from administrator.views.v1.employee_crud import (
    EmployeeDetailView,
    EmployeeListView,
    EmployeeSendEmail,
)
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"group", AdminGroupViewSet, basename="admin_group")
router.register(r"permission", AdminPermissionViewSet, basename="admin_permission")

urlpatterns = router.urls


account_router = [
    path(
        "administrator/me",
        account_views.AccountViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"},
        ),
        name="administrator-user-account",
    ),
]

generic_urls = [
    path("employee/", EmployeeListView.as_view(), name="admin_employee"),
    path(
        "employee/<uuid:pk>/",
        EmployeeDetailView.as_view(),
        name="admin_employee_detail",
    ),
    path(
        "employee/<uuid:pk>/send_email/",
        EmployeeSendEmail.as_view(),
        name="admin_employee_send_email",
    ),
]

customer_urls = [
    path("customers/", CustomerListView.as_view({"get": "list"}), name="admin_customers"),
    path(
        "customers/<uuid:pk>/",
        CustomerListView.as_view({"get": "retrieve", "delete": "destroy"}),
        name="admin_customers_remove",
    ),
    path(
        "customers/<uuid:pk>/block",
        CustomerListView.as_view({"post": "block"}),
        name="admin_customers_block",
    ),
    path(
        "customers/<uuid:pk>/unblock",
        CustomerListView.as_view({"post": "unblock"}),
        name="admin_customers_unblock",
    ),
]

developer_urls = [
    path("developers/", DeveloperListView.as_view({"get": "list"}), name="admin_developers"),
    path(
        "developers/<uuid:pk>/",
        DeveloperListView.as_view({"get": "retrieve", "delete": "destroy"}),
        name="admin_developers_remove",
    ),
    path(
        "developers/<uuid:pk>/block",
        DeveloperListView.as_view({"post": "block"}),
        name="admin_developers_block",
    ),
    path(
        "developers/<uuid:pk>/unblock",
        DeveloperListView.as_view({"post": "unblock"}),
        name="admin_developers_unblock",
    ),
]

company_urls = [
    path("company/", CompanyListView.as_view({"get": "list"}), name="admin_company"),
    path(
        "company/<uuid:pk>/",
        CompanyListView.as_view({"get": "retrieve", "delete": "destroy"}),
        name="admin_company_remove",
    ),
    path(
        "company/<uuid:pk>/block",
        CompanyListView.as_view({"post": "block"}),
        name="admin_company_block",
    ),
    path(
        "company/<uuid:pk>/unblock",
        CompanyListView.as_view({"post": "unblock"}),
        name="admin_company_unblock",
    ),
]

auth_urls = [path("login/", AdminAuthView.as_view(), name="admin_login")]


urlpatterns += account_router
urlpatterns += generic_urls
urlpatterns += customer_urls
urlpatterns += developer_urls
urlpatterns += company_urls
urlpatterns += auth_urls
