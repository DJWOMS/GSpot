from rest_framework import status

from common.models import ContactType

from base.base_tests.test_crud_contry_and_contentType import (
    BaseViewSetTestCase,
)


class CountryTestsCase(BaseViewSetTestCase):
    url: str = "/api/users/common/contact_types/"

    def setUp(self):
        super().setUp()
        self.contentType1 = ContactType.objects.create(
            name="some_contentType1",
        )
        self.contentType1 = ContactType.objects.create(
            name="some_contentType2",
        )

    def test_010_contentType_list(self):
        self.Meta.view.test_list(self.user, self)

    def test_020_retrive_contentType(self):
        pk = self.contentType1.id
        self.Meta.view.test_retrive(pk, self.user, self)

    def test_030_put_contentType(self):
        data = {
            "name": "some_contentType3",
        }
        pk = self.contentType1.id
        self.Meta.view.test_put(pk, self.admin_user, data, self)

    def test_040_create_contentType(self):
        data = {
            "name": "some_contentType3",
        }
        self.Meta.view.test_create(self.admin_user, data, self)

    def test_050_delete_contentType(self):
        self.Meta.view.test_delete(self.contentType1.id, self.admin_user, self)

    def test_060_check_permission_not_authorized_user(self):
        self.Meta.view.test_list_not_credentials(self)

    def test_070_check_permission_only_admin_user(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.user))
        response1, response2, response3 = (
            self.client.post(self.url),
            self.client.put(self.url),
            self.client.delete(self.url),
        )
        self.assertEqual(response1.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response3.status_code, status.HTTP_403_FORBIDDEN)
