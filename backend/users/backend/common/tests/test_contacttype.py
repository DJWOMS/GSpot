from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from base.models import BaseAbstractUser
from common.models import ContactType
from customer.models import CustomerUser
from developer.models import CompanyUser
from django.urls import reverse
from rest_framework import status


class ContactTypeTestsCase(BaseTestView):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("contact_types-list")
        cls.admin = cls.create_user(Admin)
        cls.user = cls.create_user(CustomerUser)
        cls.developer = cls.create_user(CompanyUser)
        cls.contacttype_1 = ContactType.objects.create(name="ContactType1")
        cls.contacttype_2 = ContactType.objects.create(name="ContactType1")

    @classmethod
    def create_user(cls, model: type[BaseAbstractUser]) -> type[BaseAbstractUser]:
        data = {
            "username": cls.faker.word(),
            "password": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "is_active": True,
        }
        if model == CustomerUser:
            data["birthday"] = cls.faker.date_object()
        if model == Admin:
            return model.objects.create_superuser(**data)
        return model.objects.create_user(**data)

    def test_010_consumer_user_can_access_list(self):
        user = self.user
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.get(f"{self.url}")
        print(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_020_developer_user_can_access_list(self):
        user = self.developer
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.get(f"{self.url}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_030_admin_user_can_access_list(self):
        user = self.admin
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.get(f"{self.url}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_040_unauthenticated_user_cannot_access_list(self):
        user = ""
        self.client.credentials(HTTP_AUTHORIZATION=user)
        response = self.client.get(f"{self.url}")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ##################################
    ###  Testing retrieve method  ####
    ##################################

    def test_50_consumer_user_can_access_retrive(self):
        user = self.user
        model_id = self.contacttype_1.id
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.get(f"{self.url}{model_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_60_consumer_user_can_access_retrive(self):
        user = self.developer
        model_id = self.contacttype_2.id
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.get(f"{self.url}{model_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_70_admin_user_can_access_retrive(self):
        user = self.admin
        model_id = self.contacttype_2.id
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.get(f"{self.url}{model_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_80_unauthenticated_user_cannot_access_retrive(self):
        user = ""
        model_id = self.contacttype_1.id
        self.client.credentials(HTTP_AUTHORIZATION=user)
        response = self.client.get(f"{self.url}{model_id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_90_get_wrong_id_retrive(self):
        user = self.admin
        model_id = ContactType.objects.count() + 1
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.get(f"{self.url}{model_id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    ##################################
    #####  Testing put method  #######
    ##################################

    def test_100_admin_user_can_access_put_and_valid_data(self):
        user = self.admin
        model_id = self.contacttype_1.id
        data = {"name": "changed ContactType"}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.put(f"{self.url}{model_id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_110_admin_user_can_access_put_and_invalid_data_var_1(self):
        user = self.admin
        model_id = self.contacttype_2.id
        data = {"name": ""}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.put(f"{self.url}{model_id}/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_120_admin_user_can_access_put_and_invalid_data_var_2(self):
        user = self.admin
        model_id = self.contacttype_2.id
        data = {"name": str("a" * 101)}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.put(f"{self.url}{model_id}/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_130_developer_user_cant_access_put(self):
        user = self.developer
        model_id = self.contacttype_1.id
        data = {"name": "some ContactType 1"}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.put(f"{self.url}{model_id}/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_140_customer_user_cant_access_put(self):
        user = self.user
        model_id = self.contacttype_2.id
        data = {"name": "some ContactType 2"}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.put(f"{self.url}{model_id}/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_150_admin_user_can_access_and_get_wrong_id_put(self):
        user = self.admin
        model_id = ContactType.objects.count() + 1
        data = {"name": "some ContactType"}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.put(f"{self.url}{model_id}/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    ##################################
    ####  Testing create method  #####
    ##################################

    def test_160_admin_user_can_access_create_and_valid_data(self):
        user = self.admin
        data = {"name": "some ContactType1"}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.post(f"{self.url}", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_170_customer_user_cant_access_create_and_valid_data(self):
        user = self.user
        data = {"name": "some ContactType2"}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.post(f"{self.url}", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_180_developer_user_cant_access_create_and_valid_data(self):
        user = self.developer
        data = {"name": "some ContactType3"}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.post(f"{self.url}", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_190_admin_user_can_access_create_and_invalid_data_var_1(self):
        user = self.admin
        data = {"name": str("a" * 101)}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.post(f"{self.url}", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_200_admin_user_can_access_create_and_invalid_data_var_2(self):
        user = self.admin
        data = {"name": ""}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.post(f"{self.url}", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    ###################################
    #####  Testing delete method  #####
    ###################################

    def test_210_admin_user_can_access_delete(self):
        user = self.admin
        model_id = self.contacttype_1.id
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.delete(f"{self.url}{model_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_220_consumer_user_cant_access_delete(self):
        user = self.user
        model_id = self.contacttype_2.id
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.delete(f"{self.url}{model_id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_230_developer_user_cant_access_delete(self):
        user = self.developer
        model_id = self.contacttype_1.id
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.delete(f"{self.url}{model_id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_240_admin_user_can_access_delete_but_wrong_id(self):
        user = self.admin
        model_id = ContactType.objects.count() + 1
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(user))
        response = self.client.delete(f"{self.url}{model_id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_250_unauthenticated_user_cannot_access_delete(self):
        user = ""
        model_id = self.contacttype_1.id
        self.client.credentials(HTTP_AUTHORIZATION=user)
        response = self.client.delete(f"{self.url}{model_id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
