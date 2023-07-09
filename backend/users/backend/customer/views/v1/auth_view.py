from base.serializers import AuthTokensResponseSerializer
from common.services.jwt.token import Token
from customer.serializers.v1.auth_serializer import CustomerAuthSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response


class CustomerAuthView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получение пользователем JWT токена",
        request_body=CustomerAuthSerializer,
        responses={
            200: AuthTokensResponseSerializer,
            400: openapi.Response(description="Email or Password not valid"),
        },
        tags=["Аутентификация", "Пользователь"],
    )
    def post(self, request):
        serializer = CustomerAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer = serializer.validated_data["user"]

        tokens = Token().generate_tokens_for_user(user=customer)

        response_serializer = AuthTokensResponseSerializer(data=tokens)
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
