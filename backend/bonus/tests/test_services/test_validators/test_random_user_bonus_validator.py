from django.contrib.auth.models import User
from django.test import TestCase

from ....models import Bonus, UserBonus
from ....services.validators.random_user_bonus_validator import RandonBonusValidator


class RandomUserBonusValidatorTestCase(TestCase):

    def setUp(self):
        self.bonus_validator = RandonBonusValidator()

    def test_is_valid(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        user1 = User.objects.create(username='Тестер1', password='123456')
        user2 = User.objects.create(username='Тестер2', password='123456')
        UserBonus.objects.create(user=user1, bonus=bonus, amount=1)
        self.assertEqual(True, self.bonus_validator.is_valid(user2))

    def test_is_no_valid(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        user = User.objects.create(username='Тестер1', password='123456')
        UserBonus.objects.create(user=user, bonus=bonus, amount=1)
        self.assertEqual(False, self.bonus_validator.is_valid(user))
