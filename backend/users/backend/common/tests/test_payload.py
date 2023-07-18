from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from base.models import BaseAbstractUser
from common.services.jwt.users_payload import PayloadFactory
from customer.models import CustomerUser
from developer.models import CompanyUser


class TestTokenJWT(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.payload_factory = PayloadFactory()
        cls.developer = cls.create_user(CompanyUser)
        cls.administrator = cls.create_user(Admin)
        cls.customer = cls.create_user(CustomerUser)

    @classmethod
    def create_user(cls, model: type[BaseAbstractUser]) -> type[BaseAbstractUser]:
        data = {
            "username": cls.faker.word(),
            "password": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
        }
        if model == CustomerUser:
            data["birthday"] = cls.faker.date_object()
        return model.objects.create_user(**data)

    def test_admin_payload(self):
        payload = self.payload_factory.create_payload(self.administrator)
        self.assertIsInstance(payload, dict)

    def test_developer_payload(self):
        payload = self.payload_factory.create_payload(self.developer)
        self.assertIsInstance(payload, dict)

    def test_customer_payload(self):
        payload = self.payload_factory.create_payload(self.customer)
        self.assertIsInstance(payload, dict)

    def test_not_base_abstract_user_instance(self):
        self.assertRaises(TypeError, self.payload_factory.create_payload, str)
