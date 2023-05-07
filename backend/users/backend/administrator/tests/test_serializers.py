from django.test import TestCase

from administrator.models import AdminPermission
from administrator.serializers.v1 import AdminGroupSerializer, AdminPermissionSerializer
from base.base_tests import BaseGroupSerializerTest, BasePermissionSerializerTest


class AdminGroupSerializerTest(BaseGroupSerializerTest, TestCase):
    @staticmethod
    def get_permission_model():
        return AdminPermission

    @staticmethod
    def get_group_serializer() -> AdminGroupSerializer:
        return AdminGroupSerializer


class AdminPermissionSerializerTest(BasePermissionSerializerTest, TestCase):
    @staticmethod
    def get_permission_serializer() -> AdminPermissionSerializer:
        return AdminPermissionSerializer
