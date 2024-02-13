from django.contrib.auth.models import User
from django.test import TestCase

from bonus.models import Bonus, UserBonus
from ...repositories.user_queries import UserQueries


class UserQueriesTestCase(TestCase):

    def setUp(self):
        self.user_queries = UserQueries()

    def test_one_user_one_bonus(self):

        user = User.objects.create(username='Тестер', password='123456')
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        UserBonus.objects.create(user=user, bonus=bonus, amount=1)
        result = list(self.user_queries.get_users())
        expected_result = [{
            'pk': user.id,
            'date_joined': user.date_joined,
            'bonuses': ['тестовый бонус1']
        }]
        self.assertEqual(expected_result, result)

    def test_one_user_two_bonus(self):

        user = User.objects.create(username='Тестер', password='123456')
        bonus1 = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        bonus2 = Bonus.objects.create(bonus_name='тестовый бонус2', is_limit=True, amount_bonus=1)
        UserBonus.objects.create(user=user, bonus=bonus1, amount=1)
        UserBonus.objects.create(user=user, bonus=bonus2, amount=1)
        result = list(self.user_queries.get_users())
        expected_result = [{
            'pk': user.id,
            'date_joined': user.date_joined,
            'bonuses': ['тестовый бонус1', 'тестовый бонус2']
        }]
        self.assertEqual(expected_result, result)

    def test_two_users(self):

        user1 = User.objects.create(username='Тестер1', password='123456')
        user2 = User.objects.create(username='Тестер2', password='123456')
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        UserBonus.objects.create(user=user1, bonus=bonus, amount=1)
        UserBonus.objects.create(user=user2, bonus=bonus, amount=1)
        result = list(self.user_queries.get_users())
        expected_result = [
            {
                'pk': user1.id,
                'date_joined': user1.date_joined,
                'bonuses': ['тестовый бонус1']
            },
            {
                'pk': user2.id,
                'date_joined': user2.date_joined,
                'bonuses': ['тестовый бонус1']
            },
        ]
        self.assertEqual(expected_result, result)

    def test_no_users(self):
        result = self.user_queries.get_users()
        expected_result = UserBonus.objects.none()
        self.assertQuerysetEqual(expected_result, result)

    def test_no_bonus(self):
        user = User.objects.create(username='Тестер', password='123456')
        result = self.user_queries.get_users()
        expected_result = [
            {
                'pk': user.id,
                'date_joined': user.date_joined,
                'bonuses': [None]
            }
        ]
        self.assertQuerysetEqual(expected_result, result)
