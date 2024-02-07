from django.contrib.auth.models import User
from django.test import TestCase

from ....models import UserBonus, Bonus
from ....repositories.user_bonus_queries import UserBonusQuery


class CreateTestCase(TestCase):

    def setUp(self):
        self.user_bonus = UserBonusQuery()

    def test_zero_amount(self):
        user = User.objects.create(username='Тестер', password='123456')
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        with self.assertRaises(ValueError):
            self.user_bonus.create(user=user, bonus=bonus, amount_bonus=0)

    def test_negative_amount(self):
        user = User.objects.create(username='Тестер', password='123456')
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        with self.assertRaises(ValueError):
            self.user_bonus.create(user=user, bonus=bonus, amount_bonus=-1)

    def test_positive(self):
        user = User.objects.create(username='Тестер', password='123456')
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        test_data = self.user_bonus.create(user=user, bonus=bonus, amount_bonus=1)
        result = UserBonus.objects.get(user=user)
        self.assertEqual(test_data, result)

    def test_duble_bonus(self):
        user = User.objects.create(username='Тестер', password='123456')
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        self.user_bonus.create(user=user, bonus=bonus, amount_bonus=1)
        self.user_bonus.create(user=user, bonus=bonus, amount_bonus=1)
        result = UserBonus.objects.filter(user=user, bonus=bonus).count()
        self.assertEqual(2, result)
