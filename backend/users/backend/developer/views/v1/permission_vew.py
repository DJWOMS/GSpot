from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from developer.models import DeveloperPermission
from developer.serializers.v1 import DeveloperPermissionSerializer


class DeveloperPermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DeveloperPermission.objects.all()
    serializer_class = DeveloperPermissionSerializer
