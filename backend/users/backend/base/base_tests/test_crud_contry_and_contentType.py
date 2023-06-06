import datetime
from random import randint
from typing import List, Union
from common.models import ContactType, Country

from administrator.models import Admin
from base.base_tests.testing_utilities.utils import MixinTestView
from customer.models import CustomerUser
from developer.models import CompanyUser


class BaseViewSetTestCase:
    url: str = ""
    admin_user: Admin
    user: CustomerUser
    company_user: CompanyUser
    valid_data_for_put: List[dict]
    invalid_data: List[dict]
    valid_data_for_create: List[dict]

    @classmethod
    def setUpTestData(cls):
        cls.admin_user = Admin.objects.create_superuser(
            username="adminR",
            email="adminR@test.com",
            phone="891123123",
            password="testpass123R",
        )
        cls.user = CustomerUser.objects.create_user(
            username="test_user",
            email="email@mail.ru",
            password="test_user1",
            first_name="user_test_name",
            last_name="user_test_name",
            phone="89991234567",
            birthday=datetime.date.today(),
        )
        cls.company_user = CompanyUser.objects.create_user(
            "company_owner",
            "company_owner@mail.ru",
            "9803489988",
            "company_owner",
        )

    class Meta:
        view: MixinTestView
        model_for_test: Union[Country, ContactType]

    @staticmethod
    def get_random_model_from_db(model: Union[Country, ContactType]) -> Union[Country, ContactType]:
        count = model.objects.count()
        if count == 0:
            raise ValueError(f"No {model.__name__} objects found in database")

        random_index = randint(0, count - 1)
        return model.objects.all()[random_index]

    @staticmethod
    def get_wrong_models_id_from_db(model: Union[Country, ContactType]) -> int:
        count = model.objects.count()
        wrong_index = count + 1
        return wrong_index

    @classmethod
    def get_random_id_model_from_db(cls, model: Union[Country, ContactType]) -> int:
        random_record = cls.get_random_model_from_db(model)
        return random_record.id

    ###################################
    #####  Testing list method  #######
    ###################################

    def test_010_1_consumer_user_can_access_list(self):
        user = self.user
        self.Meta.view.test_list_200_OK(user, self)

    def test_010_2_admin_user_can_access_list(self):
        user = self.admin_user
        self.Meta.view.test_list_200_OK(user, self)

    def test_010_3_developer_user_can_access_list(self):
        user = self.company_user
        self.Meta.view.test_list_200_OK(user, self)

    def test_010_4_unauthenticated_user_cannot_access_list(self):
        user = ""
        self.Meta.view.test_list_no_access_permission_code_403(user, self)

    ###################################
    ####  Testing retrive method  #####
    ###################################

    def test_020_1_consumer_user_cana_access_retrive(self):
        user = self.admin_user
        model_id = self.get_random_model_from_db(self.Meta.model_for_test).id
        self.Meta.view.test_retrive_200(model_id, user, self)

    def test_020_2_consumer_user_can_access_retrive(self):
        user = self.user
        model_id = self.get_random_model_from_db(self.Meta.model_for_test).id
        self.Meta.view.test_retrive_200(model_id, user, self)

    def test_020_3_admin_user_can_access_retrive(self):
        user = self.admin_user
        model_id = self.get_random_model_from_db(self.Meta.model_for_test).id
        self.Meta.view.test_retrive_200(model_id, user, self)

    def test_020_4_developer_user_can_access_retrive(self):
        user = self.company_user
        model_id = self.get_random_model_from_db(self.Meta.model_for_test).id
        self.Meta.view.test_retrive_200(model_id, user, self)

    def test_020_5_get_wrong_id_retrive(self):
        user = self.admin_user
        model_id = self.get_wrong_models_id_from_db(self.Meta.model_for_test)
        self.Meta.view.test_retrive_404(model_id, user, self)

    def test_020_6_unauthenticated_user_cannot_access_retrive(self):
        user = ""
        model_id = self.get_random_model_from_db(self.Meta.model_for_test).id
        self.Meta.view.test_retrive_403(model_id, user, self)

    ###################################
    #####  Testing create method  #####
    ###################################

    def test_30_1_admin_user_can_access_create_and_valid_data(self):
        user = self.admin_user
        data = self.valid_data_for_create
        self.Meta.view.test_create_201(user, data, self)

    def test_30_2_customer_user_cant_access_create_and_valid_data(self):
        user = self.user
        data = self.valid_data_for_create
        self.Meta.view.test_create_403(user, data, self)

    def test_30_3_developer_user_cant_access_create_and_valid_data(self):
        user = self.company_user
        data = self.valid_data_for_create
        self.Meta.view.test_create_403(user, data, self)

    def test_30_14_admin_user_can_access_create_and_invalid_data(self):
        user = self.admin_user
        data_list = self.invalid_data
        self.Meta.view.test_create_400(user, data_list, self)

    ###################################
    ######  Testing put method  #######
    ###################################

    def test_40_1_admin_user_can_access_put_and_valid_data(self):
        user = self.admin_user
        model_id = self.get_random_id_model_from_db(self.Meta.model_for_test)
        data = self.valid_data_for_put
        self.Meta.view.test_put(model_id, user, data, self)

    def test_40_2_admin_user_can_access_put_and_invalid_data(self):
        user = self.admin_user
        model_id = self.get_random_id_model_from_db(self.Meta.model_for_test)
        data_list = self.invalid_data
        self.Meta.view.test_put_400(model_id, user, data_list, self)

    def test_40_4_developer_user_cant_access_put(self):
        user = self.company_user
        model_id = self.get_random_id_model_from_db(self.Meta.model_for_test)
        data = self.valid_data_for_put
        self.Meta.view.test_put_403(model_id, user, data, self)

    def test_40_5_customer_user_cant_access_put(self):
        user = self.user
        model_id = self.get_random_id_model_from_db(self.Meta.model_for_test)
        data = self.valid_data_for_put
        self.Meta.view.test_put_403(model_id, user, data, self)

    def test_40_6_admin_user_can_access_and_get_wrong_id_put(self):
        user = self.admin_user
        model_id = self.get_wrong_models_id_from_db(self.Meta.model_for_test)
        data = self.valid_data_for_put
        self.Meta.view.test_put_404(model_id, user, data, self)

    ###################################
    #####  Testing delite method  #####
    ###################################

    def test_50_1_admin_user_can_access_delite(self):
        user = self.admin_user
        model_id = self.get_random_id_model_from_db(self.Meta.model_for_test)
        self.Meta.view.test_delete_204(model_id, user, self)

    def test_50_2_consumer_user_cant_access_delite(self):
        user = self.user
        model_id = self.get_random_id_model_from_db(self.Meta.model_for_test)
        self.Meta.view.test_delete_403(model_id, user, self)

    def test_50_3_developer_user_cant_access_delite(self):
        user = self.company_user
        model_id = self.get_random_id_model_from_db(self.Meta.model_for_test)
        self.Meta.view.test_delete_403(model_id, user, self)

    def test_50_4_admin_user_can_access_delite_but_wrong_id(self):
        user = self.admin_user
        model_id = self.get_wrong_models_id_from_db(self.Meta.model_for_test)
        self.Meta.view.test_delete_404(model_id, user, self)

    def test_50_5_unauthenticated_user_cannot_access_delite(self):
        user = ""
        model_id = self.get_random_id_model_from_db(self.Meta.model_for_test)
        self.Meta.view.test_retrive_403(model_id, user, self)
