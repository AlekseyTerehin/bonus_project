from punq import Container

from backend.bonus.services.bonuses.random_bonus import RandomBonus
from .services.bonus_programs.random_bonus_program import RandomBonusProgram
from .services.savers_bonus.random_bonus_saver import RandomBonusSaver
from .services.validators.random_user_bonus_validator import RandonBonusValidator

container = Container()

container.register(RandomBonusProgram)
container.register(RandomBonusSaver)
container.register(RandonBonusValidator)


container.register(RandomBonus)
