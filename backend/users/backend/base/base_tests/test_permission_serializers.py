from base.serializers import BasePermissionSerializer


class BasePermissionSerializerTest:
    def setUp(self):
        self.data_for_creating_permission = {
            'name': 'test_name',
            'codename': 'test_codename',
        }

    def test_create_permission(self):
        permission_serializer = self.get_permission_serializer()
        serializer = permission_serializer(data=self.data_for_creating_permission)
        self.assertTrue(serializer.is_valid())

    @staticmethod
    def get_permission_serializer() -> BasePermissionSerializer:
        raise NotImplementedError
