from .bonus_programs.random_bonus_program import RandomBonusProgram
from .savers_bonus.random_bonus_saver import RandomBonusSaver
from .validators.random_user_bonus_validator import RandonBonusValidator
from ..dto.connection_bonus_dto import ConnectionBonusDTO


class BonusConnection:

    def __init__(self, bonus_name: str):
        self.__bonus_name = bonus_name

    def get_connection(self) -> ConnectionBonusDTO:
        connection = {
            'random_bonus': ConnectionBonusDTO(RandomBonusProgram(), RandonBonusValidator(), RandomBonusSaver())
        }
        return connection[self.__bonus_name]
