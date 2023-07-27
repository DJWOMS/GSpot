from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from developer.serializers.v1.assign_permission_serializer import CompanyUserPermissionSerializer

class AssignAdminPermissionsView(APIView):
    def post(self, request, format=None):
        serializer = CompanyUserPermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Permissions assigned successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
