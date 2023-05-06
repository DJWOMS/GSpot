from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from administrator.serializers.v1.serializers import AdminGroupSerializer, AdminPermissionSerializer
from administrator.models import AdminGroup, AdminPermission


class AdminGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdminGroup.objects.all()
    serializer_class = AdminGroupSerializer


class AdminPermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdminPermission.objects.all()
    serializer_class = AdminPermissionSerializer
