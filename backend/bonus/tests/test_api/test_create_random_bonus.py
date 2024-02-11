from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from ...models import Bonus, UserBonus
from ...serialazers.bonus import SerializersBonus


class APICreateRandomBonusTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='Тестер', password='123456')
        self.url = reverse('user_bonus_create')
        token = self.get_tokens_for_user(self.user)
        self.client.login(username='Тестер', password='123456')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])

    def test_get_no_bonus(self):
        with self.assertRaises(IndexError):
            self.client.get(self.url)

    def test_get_no_auth(self):
        self.client.credentials()
        self.assertEqual(self.client.get(self.url).status_code, 401)

    def test_get_already_bonus(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        UserBonus.objects.create(user=self.user, bonus=bonus, amount=1)
        self.assertEqual(self.client.get(self.url).status_code, 400)

    def test_get_bonus(self):
        bonus1 = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        bonus2 = Bonus.objects.create(bonus_name='тестовый бонус2', is_limit=False)
        expected_results = SerializersBonus([bonus1, bonus2], many=True).data
        result = self.client.get(self.url).data
        self.assertTrue(any(result == exp_result for exp_result in expected_results))

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
