from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from developer.serializers.v1.developer_registration_serializer import (
    DeveloperRegistrationSerializer,
)


class DeveloperRegistrationView(generics.CreateAPIView):
    serializer_class = DeveloperRegistrationSerializer
    permission_classes = [
        AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)
