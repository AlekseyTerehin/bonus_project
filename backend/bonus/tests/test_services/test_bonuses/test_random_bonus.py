from unittest.mock import Mock

from django.test import TestCase

from ....dto.bonus_dto import BonusDTO
from ....services.bonus_programs.random_bonus_program import RandomBonusProgram
from ....services.bonuses.random_bonus import RandomBonus
from ....services.savers_bonus.random_bonus_saver import RandomBonusSaver
from ....services.validators.random_user_bonus_validator import RandonBonusValidator


class RandomBonusTestCase(TestCase):

    def setUp(self):

        self.bonus_program = RandomBonusProgram()
        self.bonus_program.get_bonus = Mock()
        self.saver = RandomBonusSaver()
        self.saver.save = Mock()
        self.validator = RandonBonusValidator()
        self.validator.is_valid = Mock()
        self.mock_user = Mock()
        self.mock_bonus = Mock()

    def test_cleaned_data_valid(self):
        expected_result = BonusDTO(bonus=self.mock_bonus, amount=1)
        self.bonus_program.get_bonus.return_value = expected_result
        self.validator.is_valid.return_value = True
        random_program = RandomBonus(
            bonus_program=self.bonus_program,
            saver=self.saver,
            validator=self.validator,
        )
        result = random_program._RandomBonus__cleaned_data(user=self.mock_user)
        self.assertEqual(expected_result, result)

    def test_cleaned_data_no_valid(self):
        expected_result = BonusDTO(bonus=self.mock_bonus, amount=1)
        self.bonus_program.get_bonus.return_value = expected_result
        self.validator.is_valid.return_value = False
        random_program = RandomBonus(
            bonus_program=self.bonus_program,
            saver=self.saver,
            validator=self.validator,
        )
        with self.assertRaises(ValueError):
            random_program._RandomBonus__cleaned_data(user=self.mock_user)

    def test_save_db(self):

        random_program = RandomBonus(
            bonus_program=self.bonus_program,
            saver=self.saver,
            validator=self.validator,
        )
        random_program._RandomBonus__save_db(bonus=self.mock_bonus, user=self.mock_user)

    def test_add_user_bonus(self):

        random_program = RandomBonus(
            bonus_program=self.bonus_program,
            saver=self.saver,
            validator=self.validator,
        )
        random_program.add_user_bonus(user=self.mock_user)
