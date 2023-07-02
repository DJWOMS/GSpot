from base.models import BasePermission
from base.serializers import BaseGroupSerializer


class BaseGroupSerializerTest:
    def setUp(self):
        data_for_creating_permission = {
            "name": "test_name",
            "codename": "test_codename",
        }
        permission_model = self.get_permission_model()
        self.permission = permission_model.objects.create(**data_for_creating_permission)
        self.valid_data = {
            "name": "test_name",
            "permission": [self.permission.pk],
        }
        self.empty_data = {
            "name": "",
            "permission": [],
        }
        self.empty_name_data = {
            "name": "",
            "permission": [self.permission.pk],
        }
        self.empty_permission_data = {
            "name": "test_name_2",
            "permission": [],
        }
        self.invalid_permission_data = {
            "name": "test_name_3",
            "permission": ["invalid_pk"],
        }

    @staticmethod
    def get_permission_model() -> BasePermission:
        raise NotImplementedError

    def test_create_valid_group(self):
        group_serializer = self.get_group_serializer()
        serializer = group_serializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_create_group_with_empty_data(self):
        group_serializer = self.get_group_serializer()
        serializer = group_serializer(data=self.empty_data)
        self.assertFalse(serializer.is_valid())

    def test_create_group_with_empty_name(self):
        group_serializer = self.get_group_serializer()
        serializer = group_serializer(data=self.empty_name_data)
        self.assertFalse(serializer.is_valid())

    def test_create_group_with_duplicated_name(self):
        group_serializer = self.get_group_serializer()
        serializer = group_serializer(data=self.valid_data)
        serializer.is_valid()
        serializer.save()
        serializer = group_serializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_create_group_with_empty_permission(self):
        group_serializer = self.get_group_serializer()
        serializer = group_serializer(data=self.empty_permission_data)
        self.assertTrue(serializer.is_valid())

    def test_create_group_with_invalid_permission(self):
        group_serializer = self.get_group_serializer()
        serializer = group_serializer(data=self.invalid_permission_data)
        self.assertFalse(serializer.is_valid())

    @staticmethod
    def get_group_serializer() -> BaseGroupSerializer:
        raise NotImplementedError
