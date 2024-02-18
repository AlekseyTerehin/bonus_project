from django.test import TestCase

from ....models import Bonus
from ....repositories.bonus_queries import BonusQuery


class ReduceTestCase(TestCase):

    def setUp(self):
        self.bonus = BonusQuery()

    def test_negative_number(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        with self.assertRaises(ValueError):
            self.bonus.reduce(bonus=bonus, amount_reduce=0)

    def test_more_balance(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        with self.assertRaises(ValueError):
            self.bonus.reduce(bonus=bonus, amount_reduce=2)

    def test_unlimited(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=False)
        self.bonus.reduce(bonus=bonus, amount_reduce=1)
        result = Bonus.objects.get(bonus_name='тестовый бонус1')
        self.assertEqual(bonus, result)

    def test_limited(self):
        amount_reduce = 1
        bonus = Bonus.objects.create(
            bonus_name='тестовый бонус1',
            is_limit=True,
            amount_bonus=amount_reduce,
        )
        amount = bonus.amount_bonus
        self.bonus.reduce(bonus=bonus, amount_reduce=amount_reduce)
        result = Bonus.objects.get(bonus_name='тестовый бонус1').amount_bonus
        self.assertEqual(amount - amount_reduce, result)
