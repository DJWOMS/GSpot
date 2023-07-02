from base.base_tests import BaseGroupViewsTest, BasePermissionViewsTest
from base.base_tests.test_registrations import RegistrationUsersDatasetTest
from base.base_tests.tests import TestBase, TestView
from developer.models import CompanyUser, DeveloperPermission
from django.test import TestCase


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


class DeveloperRegistrationViewTest(TestView):
    url = "/api/v1/developer/registration/"


class DeveloperRegistrationTest(TestBase, TestCase):
    class Meta:
        dataset = RegistrationUsersDatasetTest
        view = DeveloperRegistrationViewTest
