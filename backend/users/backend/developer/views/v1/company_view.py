# from django.utils.decorators import method_decorator
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework import viewsets
# from rest_framework.permissions import (
#     IsAuthenticatedOrReadOnly,
#     IsAuthenticated,
#     IsAdminUser,
#     AllowAny,
# )
#
# from base.views import PartialUpdateMixin
# from developer.models import  Company
# from developer.permissions import IsAdminOrOwnerCompany
# from developer.serializers.serializers import (
#     CompanySerializer,
#     CompanyEmployeeSerializer,
# )
#
#
# @method_decorator(
#     name='list',
#     decorator=swagger_auto_schema(
#         operation_description='Список компаний',
#         tags=['Разработчик', 'Административная панель разработчика'],
#         responses={
#             200: openapi.Response('Список компаний разработчиков', CompanyEmployeeSerializer(many=True)),
#             403: openapi.Response('Отсутствуют права '),
#         },
#     ),
# )
# @method_decorator(
#     name='retrieve',
#     decorator=swagger_auto_schema(
#         operation_description='Детальное представление компании разработчика',
#         tags=['Разработчик', 'Административная панель разработчика'],
#         responses={
#             200: openapi.Response('Компания разработчика', CompanySerializer),
#             403: openapi.Response('Отсутствуют права'),
#             404: openapi.Response('Право не найдено'),
#         },
#     ),
# )
# @method_decorator(
#     name='create',
#     decorator=swagger_auto_schema(
#         operation_description='Добавить компанию',
#         tags=['Разработчик', 'Административная панель разработчика'],
#         responses={
#             201: openapi.Response('Компания', CompanySerializer),
#             400: openapi.Response('Невалидные данные'),
#             403: openapi.Response('Отсутствуют права '),
#         },
#     ),
# )
# @method_decorator(
#     name='update',
#     decorator=swagger_auto_schema(
#         operation_description='Изменить данные компании',
#         tags=['Разработчик', 'Административная панель разработчика'],
#         responses={
#             201: openapi.Response('Компания', CompanySerializer),
#             400: openapi.Response('Невалидные данные'),
#             403: openapi.Response('Отсутствуют права'),
#         },
#     ),
# )
# @method_decorator(
#     name='destroy',
#     decorator=swagger_auto_schema(
#         operation_description='Удалить компанию',
#         tags=['Разработчик', 'Административная панель разработчика'],
#         responses={
#             204: openapi.Response('Компания удалена'),
#             403: openapi.Response('Отсутствуют права'),
#             404: openapi.Response('Компания не найдена'),
#         },
#     ),
# )
# class CompanyViewSet(PartialUpdateMixin, viewsets.ModelViewSet):
#     http_method_names = ['get', 'post', 'put', 'delete']
#     queryset = Company.objects.all()
#
#     serializer_map = {
#         'default': CompanySerializer,
#         'list': CompanyEmployeeSerializer,
#         'create': CompanySerializer,
#         'retrieve': CompanySerializer,
#         'update': CompanySerializer,
#         'partial_update': CompanySerializer,
#         'destroy': CompanySerializer,
#         'employees': CompanySerializer,
#     }
#
#     permission_map = {
#         'default': [AllowAny],
#         'list': [IsAuthenticated],
#         'create': [AllowAny],
#         'retrieve': [IsAuthenticated],
#         'update': [IsAdminOrOwnerCompany],
#         'partial_update': [IsAdminOrOwnerCompany],
#         'destroy': [IsAdminOrOwnerCompany],
#         'employees': [IsAdminOrOwnerCompany],
#     }
#
#     def get_serializer_class(self):
#         return self.serializer_map.get(self.action, self.serializer_map['default'])
#
#     def get_permissions(self):
#         return [
#             permission()
#             for permission in self.permission_map.get(self.action, self.permission_map['default'])
#         ]
#
#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)

#
# class CompanyUserViewSet(PartialUpdateMixin, viewsets.ModelViewSet):
#     queryset = CompanyUser.objects.all()
#     serializer_class = CompanyUserSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             permission_classes = [IsAuthenticated]
#         elif self.action in ['create', 'update', 'partial_update', 'destroy']:
#             permission_classes = [IsAdminOrOwnerCompany]
#         else:
#             permission_classes = [IsAdminUser]
#         return [permission() for permission in permission_classes]
