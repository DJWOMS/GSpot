from rest_framework import routers

from administrator.views.v1 import AdminGroupViewSet, AdminPermissionViewSet

router = routers.DefaultRouter()
router.register(r'group', AdminGroupViewSet, basename='admin_group')
router.register(r'permission', AdminPermissionViewSet, basename='admin_permission')

urlpatterns = router.urls
