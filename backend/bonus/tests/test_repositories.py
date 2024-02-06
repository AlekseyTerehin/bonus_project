from django.test import TestCase

from ..models import Bonus
from ..repositories.bonus_queries import BonusQuery


class BonusTestCase(TestCase):

    def setUp(self):
        self.bonus = BonusQuery()

    def test_get_active_bonuses_is_null(self):
        result = self.bonus.get_active_bonuses()
        test_data = Bonus.objects.none()
        self.assertQuerysetEqual(test_data, result)

    def test_get_active_bonuses_end_bonus(self):
        Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=0)
        result = self.bonus.get_active_bonuses()
        test_data = Bonus.objects.none()
        self.assertQuerysetEqual(test_data, result)

    def test_get_active_bonuses_unlimited(self):
        Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=False)
        result = self.bonus.get_active_bonuses()
        test_data = Bonus.objects.all()
        self.assertQuerysetEqual(test_data, result)

    def test_get_active_bonuses_limited(self):
        Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        result = self.bonus.get_active_bonuses()
        test_data = Bonus.objects.all()
        self.assertQuerysetEqual(test_data, result)

    def test_get_active_bonuses_bonus_list(self):
        Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        Bonus.objects.create(bonus_name='тестовый бонус2', is_limit=False)
        result = self.bonus.get_active_bonuses()
        test_data = Bonus.objects.all()
        self.assertQuerysetEqual(test_data, result, ordered=False)

    def test_reduce_negative_number(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        with self.assertRaises(ValueError):
            self.bonus.reduce(bonus=bonus, amount_reduce=0)

    def test_reduce_more_balance(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        with self.assertRaises(ValueError):
            self.bonus.reduce(bonus=bonus, amount_reduce=2)

    def test_reduce_unlimited(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=False)
        self.bonus.reduce(bonus=bonus, amount_reduce=1)
        result = Bonus.objects.get(bonus_name='тестовый бонус1')
        self.assertEqual(bonus, result)

    def test_reduce_limited(self):
        amount_reduce = 1
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=amount_reduce)
        amount = bonus.amount_bonus
        self.bonus.reduce(bonus=bonus, amount_reduce=amount_reduce)
        result = Bonus.objects.get(bonus_name='тестовый бонус1').amount_bonus
        self.assertEqual(amount - amount_reduce, result)
