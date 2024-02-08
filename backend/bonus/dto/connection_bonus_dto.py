from dataclasses import dataclass

from ..services.bonus_programs.abstract_bonus_program import AbstractBonusProgram
from ..services.savers_bonus.Abstract_savers_user_bonus import AbstractSaversUserBonus
from ..services.validators.user_bonus_validator import UserBonusValidator


@dataclass
class ConnectionBonusDTO:
    program: AbstractBonusProgram
    saver: AbstractSaversUserBonus
    validator: UserBonusValidator = None
