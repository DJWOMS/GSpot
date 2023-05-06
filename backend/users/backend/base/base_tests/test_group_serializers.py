from base.models import BasePermission
from base.serializers import BaseGroupSerializer


class BaseGroupSerializerTest:
    def setUp(self):
        self.data_for_creating_permission = {
            'name': 'test_name',
            'codename': 'test_codename',
        }
        permission_model = self.get_permission_model()
        self.permission = permission_model.objects.create(**self.data_for_creating_permission)
        self.data_for_creating_group = {
            'name': 'test_name',
            'permission': [self.permission.pk],
        }

    @staticmethod
    def get_permission_model() -> BasePermission:
        raise NotImplementedError

    def test_create_group(self):
        group_serializer = self.get_group_serializer()
        serializer = group_serializer(data=self.data_for_creating_group)
        self.assertTrue(serializer.is_valid())

    @staticmethod
    def get_group_serializer() -> BaseGroupSerializer:
        raise NotImplementedError
