from administrator.models import AdminPermission
from administrator.serializers.v1 import AdminGroupSerializer
from base.base_tests.tests import BaseViewTestCase


class AdminPermissionGroupSerializerTest(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        permission_creating_data = {
            "name": cls.faker.word(),
            "codename": cls.faker.word(),
        }
        cls.permission = AdminPermission.objects.create(**permission_creating_data)
        cls.serializer = AdminGroupSerializer
        cls.valid_data = {
            "name": cls.faker.word(),
            "permission": [cls.permission.pk],
        }
        cls.empty_data = {
            "name": "",
            "permission": [],
        }
        cls.empty_name_data = {
            "name": "",
            "permission": [cls.permission.pk],
        }
        cls.empty_permission_data = {
            "name": cls.faker.word(),
            "permission": [],
        }
        cls.invalid_permission_data = {
            "name": cls.faker.word(),
            "permission": ["invalid_pk"],
        }

    def test_01_create_valid_group(self):
        serializer = self.serializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_02_create_group_with_empty_data(self):
        serializer = self.serializer(data=self.empty_data)
        self.assertFalse(serializer.is_valid())

    def test_03_create_group_with_empty_name(self):
        serializer = self.serializer(data=self.empty_name_data)
        self.assertFalse(serializer.is_valid())

    def test_04_create_group_with_duplicated_name(self):
        serializer = self.serializer(data=self.valid_data)
        serializer.is_valid()
        serializer.save()
        serializer = self.serializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_05_create_group_with_empty_permission(self):
        serializer = self.serializer(data=self.empty_permission_data)
        self.assertTrue(serializer.is_valid())

    def test_06_create_group_with_invalid_permission(self):
        serializer = self.serializer(data=self.invalid_permission_data)
        self.assertFalse(serializer.is_valid())
