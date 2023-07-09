from developer.views.v1 import (
    DeveloperGroupViewSet,
    DeveloperPermissionViewSet,
    account_views,
)
from developer.views.v1.auth_view import DeveloperAuthView
from developer.views.v1.company_view import CompanyAPIView
from developer.views.v1.developer_registration_view import DeveloperRegistrationView
from developer.views.v1.employee_crud import (
    DeveloperEmployeeDetailView,
    DeveloperEmployeeListView,
)
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"group", DeveloperGroupViewSet, basename="developer_group")
router.register(r"permission", DeveloperPermissionViewSet, basename="developer_permission")


urlpatterns = router.urls

account_router = [
    path(
        "developer/me",
        account_views.AccountViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"},
        ),
        name="developer-user-account",
    ),
]

generic_routes = [
    path("registration/", DeveloperRegistrationView.as_view()),
    path("employee/", DeveloperEmployeeListView.as_view(), name="developer_users_list"),
    path(
        "employee/<uuid:pk>/",
        DeveloperEmployeeDetailView.as_view(),
        name="developer_users_detail",
    ),
]

auth_routes = [path("login/", DeveloperAuthView.as_view(), name="developer_login")]

company_urls = [
    path("company/", CompanyAPIView.as_view(), name="company"),
]

urlpatterns += account_router
urlpatterns += generic_routes
urlpatterns += auth_routes
urlpatterns += company_urls
