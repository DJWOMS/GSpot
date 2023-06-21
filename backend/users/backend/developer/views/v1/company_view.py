from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
)

from base.views import PartialUpdateMixin
from developer.models import Company, CompanyUser
from developer.permissions import IsAdminOrOwnerCompany
from developer.serializers.serializers import (
    CompanySerializer,
    CompanyEmployeeSerializer,
)


class CompanyAPIView(APIView):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAdminOrOwnerCompany,)

    def get_permissions(self):
        if self.request.method.lower() == "get":
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    @method_decorator(
        name="get",
        decorator=swagger_auto_schema(
            operation_description="Просмотр списка/отдельной компании",
            tags=["Разработчик", "Административная панель разработчика"],
            responses={
                200: openapi.Response("Компания разработчика", CompanySerializer),
                404: openapi.Response("Компания не найдена"),
            },
        ),
    )
    def get(self, request, title=None, format=None):
        print(request.method.lower())
        if title:
            company = Company.objects.get(title=title)
            serializer = self.serializer_class(company, many=False)
            return Response(serializer.data)

        companies = Company.objects.all()
        serializer = self.serializer_class(companies, many=True)
        return Response(serializer.data)

    @method_decorator(
        name="post",
        decorator=swagger_auto_schema(
            operation_description="Добавить компанию",
            request_body=CompanySerializer,
            tags=["Разработчик", "Административная панель разработчика"],
            responses={
                201: openapi.Response("Компания", CompanySerializer),
                400: openapi.Response("Невалидные данные"),
                403: openapi.Response("Отсутствуют права на создание компании"),
            },
        ),
    )
    def post(self, request, *args, **kwargs):
        user = request.user
        if not isinstance(user, CompanyUser):
            return Response(
                {"error": "You are not authorized to edit this company."},
                status=status.HTTP_403_FORBIDDEN,
            )
        data = request.data.copy()
        data["created_by"] = user.id

        serializer = self.serializer_class(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @method_decorator(
        name="update",
        decorator=swagger_auto_schema(
            operation_description="Изменить данные компании",
            tags=["Разработчик", "Административная панель разработчика"],
            responses={
                200: openapi.Response("Компания", CompanySerializer),
                400: openapi.Response("Невалидные данные"),
                403: openapi.Response("Отсутствуют права"),
                404: openapi.Response("Компания не найдена"),
            },
        ),
    )
    def put(self, request, title, format=None):
        company = get_object_or_404(self.queryset, title=title)
        if company.created_by != request.user:
            return Response(
                {"error": "You are not authorized to edit this company."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = self.serializer_class(company, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, title, format=None):
        company = get_object_or_404(Company, title=title)
        if company.created_by != request.user:
            return Response(
                {"error": "You are not authorized to delete this company."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        company.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
