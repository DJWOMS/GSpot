from rest_framework.test import APIClient

from common.services.jwt.token import Token

from base.base_tests.testing_utilities.list_method_mixin_test import ListMethodTestingMixin
from base.base_tests.testing_utilities.retrive_method_mixin_tests import RetriveMethodTestingMixin
from base.base_tests.testing_utilities.delete_method_mixin_tests import DeleteMethodTestingMixin
from base.base_tests.testing_utilities.put_method_mixin_tests import PutMethodTestingMixin
from base.base_tests.testing_utilities.create_method_mixin_tests import CreateMethodTestingMixin


class MixinTestView(
    ListMethodTestingMixin,
    RetriveMethodTestingMixin,
    DeleteMethodTestingMixin,
    PutMethodTestingMixin,
    CreateMethodTestingMixin,
):
    client = APIClient()

    @staticmethod
    def get_token(user) -> str:
        context = {
            "user_id": str(user.id),
            "role": user._meta.app_label,
        }
        return Token().generate_access_token(context)
