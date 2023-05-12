from django.test import TestCase

from base.base_tests import BaseGroupViewsTest, BasePermissionViewsTest
from developer.models import DeveloperPermission, CompanyUser


class DeveloperPermissionViewTest(BasePermissionViewsTest, TestCase):
    @staticmethod
    def get_user_model() -> CompanyUser:
        return CompanyUser

    @staticmethod
    def get_permission_path() -> str:
        return "/api/v1/developer/permission/"


class DeveloperGroupViewTest(BaseGroupViewsTest, TestCase):
    @staticmethod
    def get_user_model() -> CompanyUser:
        return CompanyUser

    @staticmethod
    def get_permission_model() -> DeveloperPermission:
        return DeveloperPermission

    @staticmethod
    def get_group_path() -> str:
        return "/api/v1/developer/group/"
