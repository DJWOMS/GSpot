from base.base_tests.tests import BaseViewTestCase
from customer.models import CustomerUser
from django.urls import reverse


class CustomerChangeAccountInfoApiTestCase(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('customer-user-account')
        cls.customer_user = CustomerUser.objects.create(
            username='CustomerUser',
            email=cls.faker.email(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
            birthday=cls.faker.date_object(),
            is_active=True,
        )

    def setUp(self):
        super().setUp()

    def test_change_info_patch(self):
        self.client.force_authenticate(user=self.customer_user)
        url = self.url
        responce = self.client.get(url)
        self.assertEqual("CustomerUser", responce.data.get("username"))
        new_data = {
            "username": "CustomerUser2",
        }
        responce_change_username = self.client.put(url, data=new_data)
        self.assertEqual("CustomerUser2", responce_change_username.data.get("username"))

    def test_change_info_logout_user(self):
        url = self.url
        responce = self.client.get(url)
        self.assertEqual(403, responce.status_code)
