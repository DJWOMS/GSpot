from django.urls import reverse


class ChangeAccountInfoApiTestCase:
    def setUp(self):
        self.user = self.get_user_model()
        self.url_reverse = self.get_reverse_url()
        self.data = self.set_settings_user()
        self.first_user = self.user.objects.create(**self.data)
        self.first_user.is_active = True
        self.first_user.save()

    @staticmethod
    def set_settings_user():
        raise NotImplementedError

    @staticmethod
    def get_user_model():
        raise NotImplementedError

    @staticmethod
    def get_reverse_url():
        raise NotImplementedError

    def test_change_info_patch(self):
        self.client.force_authenticate(user=self.first_user)
        url = reverse(self.url_reverse)
        responce = self.client.get(url)
        self.assertEqual('user_of_company', responce.data.get('username'))
        new_data = {
            'username': 'user_of_company2',
        }
        responce_change_username = self.client.put(url, data=new_data)
        self.assertEqual('user_of_company2', responce_change_username.data.get('username'))

    def test_change_info_logout_user(self):
        url = reverse(self.url_reverse)
        responce = self.client.get(url)
        self.assertEqual(403, responce.status_code)
