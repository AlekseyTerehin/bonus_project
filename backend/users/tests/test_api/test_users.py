from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from bonus.models import Bonus
from bonus.repositories.user_bonus_queries import UserBonusQuery
from users.repositories.user_queries import UserQueries
from users.serializers.users import SerializersUsers


class UsersAPIViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='Тестер', password='123456')
        self.url = reverse('users')
        token = self.get_tokens_for_user(self.user)
        self.client.login(username='Тестер', password='123456')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])

    def test_get(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        UserBonusQuery().create(user=self.user, bonus=bonus, amount_bonus=1)
        users_info = UserQueries().get_users()
        expected_result = SerializersUsers(users_info, many=True).data
        result = self.client.get(path=self.url).data
        self.assertEqual(expected_result, result['results'])

    def test_get_no_auth(self):
        self.client.credentials()
        self.assertEqual(self.client.get(self.url).status_code, 401)

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
