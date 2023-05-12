from developer.views.v1 import account_views
from django.urls import path, include
from rest_framework import routers
from common import routes
from developer.views.v1.views import CompanyUserViewSet, CompanyViewSet

router = routers.DefaultRouter()
router.register(r'developer/users', CompanyUserViewSet, basename='company_users')
router.register(r'developer/companies', CompanyViewSet, basename='company')
account_routes = routes.CustomChangeInfoAccountRouter()
account_routes.register(r'developer/me', account_views.DeveloperAccountViewSet, basename='developer-user-account')
change_pass_router = routes.CustomChangePasswordRouter()
change_pass_router.register(
    r'developer/me/change-password',
    account_views.DeveloperChangePasswordViewSet,
    basename='developer-users-change-password'
)

urlpatterns = [
    path('users/', include(account_routes.urls)),
    path('users/', include(router.urls)),
    path('users/', include(change_pass_router.urls)),
]