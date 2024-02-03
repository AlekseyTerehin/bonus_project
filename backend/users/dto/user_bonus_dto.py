from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserBonusDTO:
    pk: int
    date_joined: datetime
    bonuses: list
