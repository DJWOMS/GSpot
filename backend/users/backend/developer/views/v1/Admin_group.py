from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from administrator.models import AdminGroup, Admin
from developer.serializers.v1.assign_permission_serializer import AdminGroupSerializer
from rest_framework.permissions import IsAdminUser

class AdminGroupViewSet(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
        except Admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)

        groups = admin.groups.all()
        group_serializer = AdminGroupSerializer(groups, many=True)

        return Response({"groups": group_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
        except Admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)

        group_ids = request.data.get('group_ids', [])
        admin.groups.set(AdminGroup.objects.filter(id__in=group_ids))

        return Response({"message": "Groups assigned successfully"}, status=status.HTTP_200_OK)