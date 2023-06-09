from administrator.views.v1 import account_views
from django.urls import path
from rest_framework import routers
from administrator.views.v1 import AdminGroupViewSet, AdminPermissionViewSet
from administrator.views.v1.employee_crud import (
    EmployeeListView,
    EmployeeDetailView,
    EmployeeSendEmail,
)
from administrator.views.v1.auth_view import AdminAuthView


router = routers.DefaultRouter()
router.register(r"group", AdminGroupViewSet, basename="admin_group")
router.register(r"permission", AdminPermissionViewSet, basename="admin_permission")

urlpatterns = router.urls

account_router = [
    path(
        "administrator/me",
        account_views.AccountViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"}
        ),
        name="administrator-user-account",
    ),
    path(
        "administrator/me/change-password",
        account_views.ChangePasswordViewSet.as_view({"post": "create"}),
        name="admininstrator-user-change-password",
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

auth_urls = [path("login/", AdminAuthView.as_view(), name="admin_login")]

urlpatterns += account_router
urlpatterns += generic_urls
urlpatterns += auth_urls
