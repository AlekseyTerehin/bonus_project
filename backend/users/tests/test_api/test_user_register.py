from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase


class UserRegisterTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('regis')

    def test_create_user(self):
        data = {'username': 'тестер', 'password': 123456}
        self.client.post(path=self.url, data=data)
        user = User.objects.get(username='тестер')
        self.assertEqual('тестер', user.username)

    def test_fail_create(self):
        data = {
            'username': 'ТестовыйТестТестеровичаТестирующийТестогоТестерантаТестинского',
            'password': 123456,
        }
        result = self.client.post(path=self.url, data=data)
        expected_data = {
            'errors': {
                'username': [
                    ErrorDetail(
                        string='Убедитесь, что это значение содержит не более 50 символов.',
                        code='max_length',
                    )
                ]
            }
        }
        self.assertEqual(expected_data, result.data)
