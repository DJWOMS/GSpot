from administrator.models import Admin, AdminPermission
from base.base_tests import BaseGroupViewsTest, BasePermissionViewsTest
from django.test import TestCase


class AdminPermissionViewTest(BasePermissionViewsTest, TestCase):
    @staticmethod
    def get_user_model() -> Admin:
        return Admin

    @staticmethod
    def get_permission_path() -> str:
        return "/api/v1/admin/permission/"


class AdminGroupViewTest(BaseGroupViewsTest, TestCase):
    @staticmethod
    def get_user_model() -> Admin:
        return Admin

    @staticmethod
    def get_permission_model() -> AdminPermission:
        return AdminPermission

    @staticmethod
    def get_group_path() -> str:
        return "/api/v1/admin/group/"
