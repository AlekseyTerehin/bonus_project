from django.test import TestCase

from ....models import Bonus
from ....services.bonus_programs.random_bonus_program import RandomBonusProgram


class RandomBonusTestCase(TestCase):

    def setUp(self):
        self.bonus_program = RandomBonusProgram()

    def test_logic_is_random(self):
        Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        Bonus.objects.create(bonus_name='тестовый бонус2', is_limit=True, amount_bonus=1)
        Bonus.objects.create(bonus_name='тестовый бонус3', is_limit=False)
        sequence_bonus = {self.bonus_program._RandomBonusProgram__logic_program() for _ in range(10)}
        if len(sequence_bonus) > 1:
            self.assertEqual(1, 1)
            return
        sequence_bonus = {self.bonus_program._RandomBonusProgram__logic_program() for _ in range(10)}
        self.assertEqual(len(sequence_bonus) > 1, True)
