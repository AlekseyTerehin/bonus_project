from django.contrib.auth.models import User

from ...dto.bonus_dto import BonusDTO
from ...models import UserBonus
from ...services.bonus_programs.random_bonus_program import RandomBonusProgram
from ...services.savers_bonus.random_bonus_saver import RandomBonusSaver
from ...services.validators.random_user_bonus_validator import RandonBonusValidator


class RandomBonus:

    def __init__(
        self,
        bonus_program: RandomBonusProgram,
        saver: RandomBonusSaver,
        validator: RandonBonusValidator,
    ):
        self.__bonus_program = bonus_program
        self.__saver = saver
        self.__validator = validator

    def add_user_bonus(self, user: User) -> UserBonus:
        bonus_for_user = self.__cleaned_data(user=user)
        user_bonuses = self.__save_db(bonus=bonus_for_user, user=user)
        return user_bonuses

    def __cleaned_data(self, user: User) -> BonusDTO:
        bonus_for_user = self.__bonus_program.get_bonus()

        if not self.__validator.is_valid(user=user):
            raise ValueError(self.__validator.message_error)

        return bonus_for_user

    def __save_db(self, bonus: BonusDTO, user: User) -> UserBonus:
        return self.__saver.save(data=bonus, user=user)
