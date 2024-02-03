from .abstract_validator import AbstractValidator
from ...repositories.user_bonus_queries import UserBonusQuery


class UserBonusValidator(AbstractValidator):

    def __init__(self):
        super().__init__()
        self.queryset = UserBonusQuery()
