from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from customer.serializers.v1.auth_serializer import CustomerAuthSerializer

from common.services.jwt.token import Token


class CustomerAuthView(APIView):
    permission_classes = [AllowAny]

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

        return Response(tokens, status=status.HTTP_200_OK)
