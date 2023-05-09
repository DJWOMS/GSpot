from django.urls import path, include
from rest_framework import routers

from developer.views.v1 import (
    CompanyUserViewSet,
    CompanyViewSet,
    DeveloperGroupViewSet,
    DeveloperPermissionViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', CompanyUserViewSet, basename='company_users')
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'group', DeveloperGroupViewSet, basename='developer_group')
router.register(r'permission', DeveloperPermissionViewSet, basename='developer_permission')

urlpatterns = router.urls
