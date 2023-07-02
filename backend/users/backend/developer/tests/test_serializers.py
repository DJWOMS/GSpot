from base.base_tests import BaseGroupSerializerTest, BasePermissionSerializerTest
from developer.models import DeveloperPermission
from developer.serializers.v1 import (
    DeveloperGroupSerializer,
    DeveloperPermissionSerializer,
)
from django.test import TestCase


class DeveloperGroupSerializerTest(BaseGroupSerializerTest, TestCase):
    @staticmethod
    def get_permission_model():
        return DeveloperPermission

    @staticmethod
    def get_group_serializer() -> DeveloperGroupSerializer:
        return DeveloperGroupSerializer


class DeveloperPermissionSerializerTest(BasePermissionSerializerTest, TestCase):
    @staticmethod
    def get_permission_serializer() -> DeveloperPermissionSerializer:
        return DeveloperPermissionSerializer
