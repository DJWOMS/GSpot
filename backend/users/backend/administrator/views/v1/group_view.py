from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from administrator.serializers.v1 import AdminGroupSerializer
from administrator.models import AdminGroup


class AdminGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdminGroup.objects.all()
    serializer_class = AdminGroupSerializer
