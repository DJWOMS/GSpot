from administrator.serializers.v1 import AdminPermissionSerializer
from base.base_tests.tests import BaseTestView


class AdminPermissionSerializerTest(BaseTestView):
    def setUp(self):
        self.valid_data = {
            "name": self.faker.word(),
            "codename": self.faker.word(),
        }
        self.empty_data = {
            "name": "",
            "codename": "",
        }
        self.empty_name_data = {
            "name": "",
            "codename": self.faker.word(),
        }
        self.empty_codename_data = {
            "name": self.faker.word(),
            "codename": "",
        }

    @staticmethod
    def get_permission_serializer() -> AdminPermissionSerializer:
        return AdminPermissionSerializer

    def test_01_create_permission(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_02_create_permission_with_empty_data(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.empty_data)
        self.assertFalse(serializer.is_valid())

    def test_03_create_permission_with_empty_name(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.empty_name_data)
        self.assertFalse(serializer.is_valid())

    def test_04_create_permission_with_duplicated_name(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.valid_data)
        serializer.is_valid()
        serializer.save()
        serializer = permission_serializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_05_create_permission_with_empty_codename(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.empty_codename_data)
        self.assertFalse(serializer.is_valid())
