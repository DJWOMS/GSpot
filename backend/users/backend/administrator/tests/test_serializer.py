from administrator.serializers.v1 import AdminPermissionSerializer
from base.base_tests.tests import BaseViewTestCase


class AdminPermissionSerializerTest(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.valid_data = {
            "name": cls.faker.word(),
            "codename": cls.faker.word(),
        }
        cls.empty_data = {
            "name": "",
            "codename": "",
        }
        cls.empty_name_data = {
            "name": "",
            "codename": cls.faker.word(),
        }
        cls.empty_codename_data = {
            "name": cls.faker.word(),
            "codename": "",
        }
        cls.serializer = AdminPermissionSerializer

    def test_01_create_permission(self):
        serializer = self.serializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_02_create_permission_with_empty_data(self):
        serializer = self.serializer(data=self.empty_data)
        self.assertFalse(serializer.is_valid())

    def test_03_create_permission_with_empty_name(self):
        serializer = self.serializer(data=self.empty_name_data)
        self.assertFalse(serializer.is_valid())

    def test_04_create_permission_with_duplicated_name(self):
        serializer = self.serializer(data=self.valid_data)
        serializer.is_valid()
        serializer.save()
        serializer = self.serializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_05_create_permission_with_empty_codename(self):
        serializer = self.serializer(data=self.empty_codename_data)
        self.assertFalse(serializer.is_valid())
