from typing import Iterable, Tuple

from .abstract_bonus_program import AbstractBonusProgram
from ...dto.bonus_dto import BonusDTO
from ...models import Bonus
from ...repositories.bonus_queries import BonusQuery


class RandomBonusProgram(AbstractBonusProgram):

    def __init__(self):
        super().__init__()
        self.__queryset = BonusQuery().get_active_bonuses()

    def __logic_program(self) -> Tuple[Bonus, int]:
        try:
            amount_bonus = 1
            return self.__queryset.order_by('?')[0], amount_bonus
        except IndexError:
            raise IndexError('Бонусов не осталось')

    def get_bonus(self) -> BonusDTO:
        return BonusDTO(*self.__logic_program())
