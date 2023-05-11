from administrator.models import Admin
from administrator.serializers.v1.employee_crud import (
    EmployeeCreateUpdateSerializer,
    EmployeeRetrieveSerializer,
)
from base.base_tests.test_employee import (
    BaseDatasetTest,
    BaseTest,
    BaseSerializerTest,
    BaseViewTest,
)
from django.test import TestCase

from common.models import Country


class AdminEmployeeDataset(BaseDatasetTest):
    @classmethod
    def perform_create(cls):
        Country.objects.create(id=1, name='Russia')

    created_data = [
        {
            'username': 'created_employee',
            'country_id': 1,
            'email': 'created_employee@gmail.com',
            'phone': '9995558989',
            'is_banned': False,
        }
    ]

    valid_data = [
        {
            'username': 'test_employee',
            'country': 1,
            'email': 'user@gmail.com',
            'phone': '9995556767',
            'is_banned': False,
        },
    ]

    invalid_data = [
        {
            'country': 2,
            'is_superuser': False,
            'email': 'user@gmail.com',
            'phone': '992222222295556767',
            'is_banned': False,
        },
        {
            'country': 1,
            'username': 'gravity',
            'email': '@gmail.com',
            'phone': '99226666226767',
            'is_banned': False,
        },
        {
            'is_superuser': False,
        },
    ]


class AdminSerializerSerializerTest(BaseSerializerTest):
    serializer_map = {
        'default': EmployeeCreateUpdateSerializer,
        'retrieve': EmployeeRetrieveSerializer,
    }


class AdminViewTest(BaseViewTest):
    url = '/api/v1/admin/employee/'
    methods = ['get', 'post']
    users_pass = {
        'default': 'AdminSuperUser',
    }


class AdminEmployeeTest(BaseTest, TestCase):
    model = Admin

    class Meta:
        dataset = AdminEmployeeDataset
        serializer = AdminSerializerSerializerTest
        view = AdminViewTest
