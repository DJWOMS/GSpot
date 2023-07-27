from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from administrator.models import AdminPermission, Admin
from developer.serializers.v1.assign_permission_serializer import AdminPermissionSerializer
from rest_framework.permissions import IsAdminUser

class AdminPermissionViewSet(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
        except Admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)

        permissions = admin.user_permissions.all()
        permission_serializer = AdminPermissionSerializer(permissions, many=True)

        return Response({"permissions": permission_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
        except Admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)

        permission_ids = request.data.get('permission_ids', [])
        admin.user_permissions.set(AdminPermission.objects.filter(id__in=permission_ids))

        return Response({"message": "Permissions assigned successfully"}, status=status.HTTP_200_OK)
