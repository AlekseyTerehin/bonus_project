from django.test import TestCase

from ...models import Bonus
from ...serialazers.bonus import SerializersBonus


class BonusSerialazersTestCase(TestCase):

    def test_ok(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        result = SerializersBonus(bonus).data
        expected_result = {'bonus_name': 'тестовый бонус1'}
        self.assertEqual(expected_result, result)
