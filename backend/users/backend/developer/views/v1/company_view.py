from django.http import Http404

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.permissions.permissons import CompanyOwnerPerm, IsCompanySuperUserPerm
from developer.models import Company
from developer.serializers.v1.company_serializer import (
    CompanySerializer,
    CompanyCreateSerializer,
)

post_method_schema = swagger_auto_schema(
    operation_description="Добавить компанию",
    request_body=CompanyCreateSerializer,
    tags=["Разработчик", "Административная панель разработчика"],
    responses={
        201: openapi.Response("Компания", CompanyCreateSerializer),
        401: openapi.Response("Не аутентифицированный пользователь"),
        403: openapi.Response("Отсутствуют права на просмотр"),
    },
)

put_method_schema = swagger_auto_schema(
    operation_description="Изменить данные компании",
    request_body=CompanySerializer,
    tags=["Разработчик", "Административная панель разработчика"],
    responses={
        200: openapi.Response("Компания", CompanySerializer),
        400: openapi.Response("Невалидные данные"),
        403: openapi.Response("Отсутствуют права"),
        404: openapi.Response("Компания не найдена"),
    },
)

delete_method_schema = swagger_auto_schema(
    operation_description="Удалить компанию",
    tags=["Разработчик", "Административная панель разработчика"],
    responses={
        204: openapi.Response("Пользователь удалён"),
        403: openapi.Response("Отсутствуют права на удаление"),
        404: openapi.Response("Компания не найден"),
    },
)


class CompanyListAPIView(APIView):
    http_method_names = ["post"]
    permission_classes = (IsCompanySuperUserPerm,)

    @post_method_schema
    def post(self, request, *args, **kwargs):
        serializer = CompanyCreateSerializer(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyDetailAPIView(APIView):
    http_method_names = ["put", "delete"]
    permission_classes = (CompanyOwnerPerm,)

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    @put_method_schema
    def put(self, request, pk, format=None):
        company = self.get_object(pk=pk)

        serializer = CompanySerializer(company, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @delete_method_schema
    def delete(self, request, pk, format=None):
        company = self.get_object(pk=pk)

        company.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
