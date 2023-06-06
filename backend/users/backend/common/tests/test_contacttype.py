from django.test import TestCase

from base.base_tests.test_crud_contry_and_contentType import BaseViewSetTestCase
from base.base_tests.testing_utilities.utils import MixinTestView
from common.models import ContactType
from common.tests.factory import ContactTypeFactory


class ContactTypeTestsCase(BaseViewSetTestCase, TestCase):
    url: str = "/api/users/common/contact_types/"
    valid_data_for_put = [{"name": "renamed contactType1"}, {"name": "renamed contactType2"}]
    invalid_data = [{"name": ""}, {"name": str("a" * 101)}]
    valid_data_for_create = [{"name": "some contentType 1"}, {"name": "some contentType 1"}]

    @classmethod
    def setUpClass(cls):
        cls.countries = ContactTypeFactory.create_batch(5)
        super().setUpClass()

    class Meta:
        view: MixinTestView = MixinTestView
        model_for_test: ContactType = ContactType
