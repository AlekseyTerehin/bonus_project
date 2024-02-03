from dataclasses import dataclass

from ..models import Bonus


@dataclass
class BonusDTO:
    bonus: Bonus
    amount: int
