from common.serializers.v1.totp_serializer import CheckTOTPSerializer
from common.tasks import create_payment_account
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        request_body=CheckTOTPSerializer,
        operation_description="Проверка валидности TOTP токена",
        tags=["Аутентификация", "Администратор", "Разработчик", "Пользователь"],
        responses={
            200: openapi.Response("Токен валиден", CheckTOTPSerializer),
            400: openapi.Response("Токен не найден"),
        },
    ),
)
class CheckTOTPView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    http_method_names = ["post"]

    def post(self, request):
        serializer = CheckTOTPSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # get user uuid and push to payments
        user_uuid = serializer.validated_data["user"]["id"]
        create_payment_account(user_uuid)

        return Response(serializer.data, status=status.HTTP_200_OK)
