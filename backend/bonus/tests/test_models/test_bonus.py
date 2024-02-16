from unittest import TestCase

from bonus.models import Bonus


class BonusModelTestCase(TestCase):

    def test_name_obj(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус', is_limit=True, amount_bonus=1)
        self.assertEqual('тестовый бонус', bonus.__str__())
