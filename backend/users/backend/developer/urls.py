from developer.views.v1 import account_views
from django.urls import path, include
from rest_framework import routers
from common import routes
from developer.views.v1.views import (
    CompanyUserViewSet,
    CompanyViewSet,
)
from developer.views.v1.developer_registration_view import DeveloperRegistrationView
from developer.views.v1 import DeveloperGroupViewSet
from developer.views.v1 import DeveloperPermissionViewSet

router = routers.DefaultRouter()
router.register(r'developer/users', CompanyUserViewSet, basename='company_users')
router.register(r'developer/companies', CompanyViewSet, basename='company')
router.register(r'group', DeveloperGroupViewSet, basename='developer_group')
router.register(r'permission', DeveloperPermissionViewSet, basename='developer_permission')

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

urlpatterns = [
    path('users/', include(router.urls)),
    path('registration/', DeveloperRegistrationView.as_view()),
]

urlpatterns += account_router
