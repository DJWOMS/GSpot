from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from base.serializers import AuthTokensResponseSerializer
from customer.serializers.v1.auth_serializer import CustomerAuthSerializer

from common.services.jwt.token import Token


class CustomerAuthView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=CustomerAuthSerializer,
        responses={
            200: AuthTokensResponseSerializer,
            400: openapi.Response(description="Email or Password not valid"),
        },
        tags=["Аутентификация Customer"],
    )
    def post(self, request):
        serializer = CustomerAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer = serializer.validated_data["user"]
        data = {
            "user_id": str(customer.id),
            "role": customer._meta.app_label,
            "avatar": str(customer.avatar),
            "age": customer.age,
        }

        tokens = Token().generate_tokens(data=data)

        response_serializer = AuthTokensResponseSerializer(data=tokens)
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
