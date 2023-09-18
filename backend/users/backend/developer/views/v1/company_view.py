from common.permissions.permissons import CompanyOwnerPerm, IsCompanySuperUserPerm
from developer.models import Company
from developer.serializers.v1.company_serializer import (
    CompanyCreateSerializer,
    CompanySerializer,
    CompanyUpdateSerializer,
)
from django.http import Http404
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

get_method_schema = swagger_auto_schema(
    operation_description="Получить содержимое собственной компании владельцем компании",
    tags=["Разработчик", "Административная панель разработчика"],
    responses={
        200: openapi.Response("Просмотр собственной компании"),
        403: openapi.Response("Отсутствуют права на просмотр"),
    },
)

post_method_schema = swagger_auto_schema(
    operation_description="Добавить компанию",
    tags=["Разработчик", "Административная панель разработчика"],
    responses={
        201: openapi.Response("Компания"),
        401: openapi.Response("Не аутентифицированный пользователь"),
        403: openapi.Response("Отсутствуют права на просмотр"),
    },
)

put_method_schema = swagger_auto_schema(
    operation_description="Изменить данные компании",
    tags=["Разработчик", "Административная панель разработчика"],
    responses={
        200: openapi.Response("Компания"),
        400: openapi.Response("Невалидные данные"),
        403: openapi.Response("Отсутствуют права"),
        404: openapi.Response("Компания не найдена"),
    },
)

delete_method_schema = swagger_auto_schema(
    operation_description="Удалить компанию",
    tags=["Разработчик", "Административная панель разработчика"],
    responses={
        204: openapi.Response("Компания удалена"),
        403: openapi.Response("Отсутствуют права на удаление"),
        404: openapi.Response("Компания не создана"),
    },
)


class CompanyAPIView(APIView):
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = (IsCompanySuperUserPerm,)

    @get_method_schema
    def get(self, request):
        user = request.user
        company = get_object_or_404(Company, created_by=user)
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)

    @post_method_schema
    def post(self, request, *args, **kwargs):
        serializer = CompanyCreateSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @put_method_schema
    def put(self, request):
        user = request.user
        company = get_object_or_404(Company, created_by=user)
        serializer = CompanyUpdateSerializer(company, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @delete_method_schema
    def delete(self, request):
        user = request.user
        company = get_object_or_404(Company, created_by=user)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
