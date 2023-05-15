from django.urls import path, include
from rest_framework import routers

from developer.views.v1 import (
    CompanyUserViewSet,
    CompanyViewSet,
    DeveloperGroupViewSet,
    DeveloperPermissionViewSet,
)
from developer.views.v1.developer_registration_view import DeveloperRegistrationView
from developer.views.v1.employee_crud import DeveloperEmployeeListView

router = routers.DefaultRouter()
router.register(r'users', CompanyUserViewSet, basename='company_users')
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'group', DeveloperGroupViewSet, basename='developer_group')
router.register(r'permission', DeveloperPermissionViewSet, basename='developer_permission')

urlpatterns = router.urls

generic_routes = [
    path('registration/', DeveloperRegistrationView.as_view()),
    path('employee/', DeveloperEmployeeListView.as_view(), name='developer_users_list'),
]

urlpatterns += generic_routes
