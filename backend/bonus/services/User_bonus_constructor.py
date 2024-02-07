from typing import List, Sequence

from django.contrib.auth.models import User
from django.db import transaction

from .bonus_connection import BonusConnection
from ..dto.bonus_dto import BonusDTO
from ..models import UserBonus


class UserBonusConstructor:

    def __init__(self, user: User, bonus_name):
        self.user = user
        self.__connection = BonusConnection(bonus_name=bonus_name).get_connection()
        self.__bonus_program = self.__connection.program
        self.__validator = self.__connection.validator
        self.__saver = self.__connection.saver

    def add_user_bonus(self) -> List[UserBonus]:
        bonuses_for_user = self.__cleaned_data()
        with transaction.atomic():
            user_bonuses = [self.__save_db(bonus=bonus) for bonus in bonuses_for_user]
        return user_bonuses

    def __cleaned_data(self) -> Sequence[BonusDTO]:
        bonuses_for_user = self.__bonus_program.get_bonuses()

        if not self.__validator:
            return bonuses_for_user

        if not self.__validator.is_valid(user=self.user):
            raise ValueError(self.__validator.message_error)

        return bonuses_for_user

    def __save_db(self, bonus: BonusDTO) -> UserBonus:
        return self.__saver.save(data=bonus, user=self.user)
