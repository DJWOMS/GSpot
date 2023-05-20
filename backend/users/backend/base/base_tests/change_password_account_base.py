from django.urls import reverse


class ChangePasswordAccountInfoApiTestCase:
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

    def test_change_password_currect_patch(self):
        self.client.force_authenticate(user=self.first_user)
        url = reverse(self.url_reverse)
        self.first_user.set_password('usercompany')
        data = {
            'old_password': 'usercompany',
            'new_password': 'adminnew01',
            'confirmation_new_password': 'adminnew01',
        }
        self.client.post(url, data=data)
        self.assertTrue(self.first_user.check_password('adminnew01'))

    def test_change_password_wrong_old_password(self):
        self.client.force_authenticate(user=self.first_user)
        url = reverse(self.url_reverse)
        self.first_user.set_password('usercompany')
        data = {
            'old_password': 'comanyuser',
            'new_password': 'adminnew01',
            'confirmation_new_password': 'adminnew01',
        }
        responce = self.client.post(url, data=data)
        self.assertEqual(400, responce.status_code)
        self.assertEqual(
            'Please check that your current password is correct', responce.json().get('detail')
        )

    def test_change_password_wrong_confirm_password(self):
        self.client.force_authenticate(user=self.first_user)
        url = reverse(self.url_reverse)
        self.first_user.set_password('usercompany')
        data = {
            'old_password': 'usercompany',
            'new_password': 'adminnew01',
            'confirmation_new_password': 'adminnew',
        }
        responce = self.client.post(url, data=data)
        self.assertEqual(400, responce.status_code)
        self.assertEqual(
            'The confirmation password does not match the new password',
            responce.json().get('detail'),
        )

    def test_change_password_logout_user(self):
        url = reverse(self.url_reverse)
        responce = self.client.get(url)
        self.assertEqual(403, responce.status_code)
