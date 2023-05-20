from django.urls import path, include
from administrator.views.v1 import account_views
from common import routes
from rest_framework import routers
from administrator.views.v1 import AdminGroupViewSet, AdminPermissionViewSet

router = routers.DefaultRouter()
router.register(r'group', AdminGroupViewSet, basename='admin_group')
router.register(r'permission', AdminPermissionViewSet, basename='admin_permission')

urlpatterns = router.urls

account_router = [
    path(
        'administrator/me',
        account_views.AccountViewSet.as_view(
            {'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'}
        ),
        name='administrator-user-account',
    ),
    path(
        'administrator/me/change-password',
        account_views.ChangePasswordViewSet.as_view({'post': 'create'}),
        name='admininstrator-user-change-password',
    ),
]

urlpatterns += account_router
