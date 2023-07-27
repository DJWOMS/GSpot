from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from administrator.models import AdminPermission, AdminGroup, Admin
from developer.serializers.v1.assign_permission_serializer import AdminPermissionSerializer, AdminGroupSerializer
from rest_framework.permissions import IsAdminUser

class AdminPermissionViewSet(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
        except Admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)

        # Get the admin's permissions and groups
        permissions = admin.admin_permissions.all()
        groups = admin.admin_groups.all()

        permission_serializer = AdminPermissionSerializer(permissions, many=True)
        group_serializer = AdminGroupSerializer(groups, many=True)

        return Response({
            "permissions": permission_serializer.data,
            "groups": group_serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request, admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
        except Admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)

        # Here you can process the request data to assign permissions and groups to the admin
        # For example, you may receive lists of permission and group IDs and associate them with the admin.

        # For demonstration purposes, assume we receive lists of permission and group IDs from the request data
        permission_ids = request.data.get('permission_ids', [])
        group_ids = request.data.get('group_ids', [])

        admin.admin_permissions.set(AdminPermission.objects.filter(id__in=permission_ids))
        admin.admin_groups.set(AdminGroup.objects.filter(id__in=group_ids))

        return Response({"message": "Permissions and groups assigned successfully"}, status=status.HTTP_200_OK)