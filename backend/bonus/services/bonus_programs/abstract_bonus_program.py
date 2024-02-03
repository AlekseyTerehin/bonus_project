from typing import Sequence, Any

from ...dto.bonus_dto import BonusDTO


class AbstractBonusProgram:

    def __init__(self):
        self.__queryset = None

    def __logic_program(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    def get_bonuses(self) -> Sequence[BonusDTO]:
        raise NotImplementedError
