from django.contrib.auth.models import User
from django.test import TestCase

from ....models import UserBonus, Bonus
from ....repositories.user_bonus_queries import UserBonusQuery


class CheckUserBonusTestCase(TestCase):

    def setUp(self):
        self.user_bonus = UserBonusQuery()

    def test_there_is_bonus(self):
        user = User.objects.create(username='Тестер', password='123456')
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        UserBonus.objects.create(user=user, bonus=bonus, amount=1)
        result = self.user_bonus.check_user_bonus(user)
        self.assertEqual(True, result)

    def test_no_bonus(self):
        user1 = User.objects.create(username='Тестер1', password='123456')
        user2 = User.objects.create(username='Тестер2', password='123456')
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        UserBonus.objects.create(user=user1, bonus=bonus, amount=1)
        result = self.user_bonus.check_user_bonus(user2)
        self.assertEqual(False, result)
