from developer.views.v1 import account_views
from django.urls import path, include
from rest_framework import routers
from developer.views.v1.views import (
    CompanyUserViewSet,
    CompanyViewSet,
)
from developer.views.v1.developer_registration_view import DeveloperRegistrationView
from developer.views.v1 import DeveloperGroupViewSet
from developer.views.v1 import DeveloperPermissionViewSet
from developer.views.v1.employee_crud import DeveloperEmployeeListView, DeveloperEmployeeDetailView


router = routers.DefaultRouter()
router.register(r'developer/users', CompanyUserViewSet, basename='company_users')
router.register(r'developer/companies', CompanyViewSet, basename='company')
router.register(r'group', DeveloperGroupViewSet, basename='developer_group')
router.register(r'permission', DeveloperPermissionViewSet, basename='developer_permission')

urlpatterns = router.urls

account_router = [
    path(
        'developer/me',
        account_views.AccountViewSet.as_view(
            {'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'}
        ),
        name='developer-user-account',
    ),
    path(
        'developer/me/change-password',
        account_views.ChangePasswordViewSet.as_view({'post': 'create'}),
        name='developer-user-change-password',
    ),
]

generic_routes = [
    path('registration/', DeveloperRegistrationView.as_view()),
    path('employee/', DeveloperEmployeeListView.as_view(), name='developer_users_list'),
    path(
        'employee/<uuid:pk>/', DeveloperEmployeeDetailView.as_view(), name='developer_users_detail'
    ),
]

urlpatterns += account_router
urlpatterns += generic_routes
