from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from developer.models import DeveloperGroup
from developer.serializers.v1 import DeveloperGroupSerializer


class DeveloperGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DeveloperGroup.objects.all()
    serializer_class = DeveloperGroupSerializer
