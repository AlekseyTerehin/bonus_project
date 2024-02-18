from bonus.models import Bonus, UserBonus
from django.contrib.auth.models import User
from django.test import TestCase
from users.repositories.user_queries import UserQueries
from users.serializers.users import SerializersUsers


class RegisterUserSerializerTestCase(TestCase):

    def test_ok(self):
        user = User.objects.create(username='Тестер', password='123456')
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        UserBonus.objects.create(user=user, bonus=bonus, amount=1)
        data = UserQueries().get_users()

        result = list(SerializersUsers(data, many=True).data[0].keys())

        expected_result = ['pk', 'date_joined', 'bonuses']
        self.assertEqual(expected_result, result)
