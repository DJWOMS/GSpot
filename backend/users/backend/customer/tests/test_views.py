from base.base_tests.test_registrations import RegistrationUsersDatasetTest
from base.base_tests.tests import TestBase, TestView
from django.test import TestCase


class CustomerRegistrationViewTest(TestView):
    url = "/api/v1/customer/registration/"


class CustomerRegistrationTest(TestBase, TestCase):
    class Meta:
        dataset = RegistrationUsersDatasetTest
        view = CustomerRegistrationViewTest
