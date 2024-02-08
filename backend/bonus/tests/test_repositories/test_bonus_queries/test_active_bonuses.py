from django.test import TestCase

from ....models import Bonus
from ....repositories.bonus_queries import BonusQuery


class ActiveBonusesTestCase(TestCase):

    def setUp(self):
        self.bonus = BonusQuery()

    def test_is_null(self):
        result = self.bonus.get_active_bonuses()
        test_data = Bonus.objects.none()
        self.assertQuerysetEqual(test_data, result)

    def test_end_bonus(self):
        Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=0)
        result = self.bonus.get_active_bonuses()
        test_data = Bonus.objects.none()
        self.assertQuerysetEqual(test_data, result)

    def test_unlimited(self):
        Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=False)
        result = self.bonus.get_active_bonuses()
        test_data = Bonus.objects.all()
        self.assertQuerysetEqual(test_data, result)

    def test_limited(self):
        Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        result = self.bonus.get_active_bonuses()
        test_data = Bonus.objects.all()
        self.assertQuerysetEqual(test_data, result)

    def test_bonus_list(self):
        Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        Bonus.objects.create(bonus_name='тестовый бонус2', is_limit=False)
        result = self.bonus.get_active_bonuses()
        test_data = Bonus.objects.all()
        self.assertQuerysetEqual(test_data, result, ordered=False)
