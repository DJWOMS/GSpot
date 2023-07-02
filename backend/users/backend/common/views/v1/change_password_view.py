from common.serializers.v1.change_password_serializer import ChangePasswordSerializers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

post_method_schema = swagger_auto_schema(
    operation_description="Изменение пароля пользователя",
    tags=["Разработчик", "Личный кабинет разработчика"],
    responses={
        200: openapi.Response("пароль успешно изменён"),
        401: openapi.Response("Не аутентифицированный пользователь"),
    },
)


class ChangePasswordAPIView(APIView):
    http_method_names = ["post"]
    permission_classes = (IsAuthenticated,)

    @post_method_schema
    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializers(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        serializer.create(serializer.validated_data)

        return Response({"success": "Password changed successfully"}, status=status.HTTP_200_OK)
