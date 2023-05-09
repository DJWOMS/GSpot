from base.serializers import BasePermissionSerializer


class BasePermissionSerializerTest:
    def setUp(self):
        self.valid_data = {
            'name': 'test_name',
            'codename': 'test_codename',
        }
        self.empty_data = {
            'name': '',
            'codename': '',
        }
        self.empty_name_data = {
            'name': '',
            'codename': 'test_codename',
        }
        self.empty_codename_data = {
            'name': 'test_name',
            'codename': '',
        }

    def test_create_permission(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_create_permission_with_empty_data(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.empty_data)
        self.assertFalse(serializer.is_valid())

    def test_create_permission_with_empty_name(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.empty_name_data)
        self.assertFalse(serializer.is_valid())

    def test_create_permission_with_duplicated_name(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.valid_data)
        serializer.is_valid()
        serializer.save()
        serializer = permission_serializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_create_permission_with_empty_codename(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.empty_codename_data)
        self.assertFalse(serializer.is_valid())

    @staticmethod
    def get_permission_serializer() -> BasePermissionSerializer:
        raise NotImplementedError
