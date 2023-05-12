from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from administrator.serializers.v1 import AdminPermissionSerializer
from administrator.models import AdminPermission


class AdminPermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdminPermission.objects.all()
    serializer_class = AdminPermissionSerializer
