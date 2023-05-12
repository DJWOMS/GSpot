from django.urls import path, include
from administrator.views.v1 import account_views
from common import routes

router = routes.CustomChangeInfoAccountRouter()
router.register(r'administrator/me', account_views.AdministratorAccountViewSet, basename='administrator-user-account')
change_pass_router = routes.CustomChangePasswordRouter()
change_pass_router.register(
    r'administrator/me/change-password',
    account_views.AdministratorChangePasswordViewSet,
    basename='admininstrator-users-change-password'
)
urlpatterns = [
    path('users/', include(change_pass_router.urls)),
    path('users/', include(router.urls)),
]