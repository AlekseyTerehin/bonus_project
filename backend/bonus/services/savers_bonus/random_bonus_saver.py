from django.contrib.auth.models import User
from django.db import transaction

from .Abstract_savers_user_bonus import AbstractSaversUserBonus
from ...dto.bonus_dto import BonusDTO
from ...models import UserBonus
from ...repositories.bonus_queries import BonusQuery
from ...repositories.user_bonus_queries import UserBonusQuery


class RandomBonusSaver(AbstractSaversUserBonus):

    def save(self, data: BonusDTO, user: User) -> UserBonus:
        with transaction.atomic():
            BonusQuery().reduce(bonus=data.bonus, amount_reduce=data.amount)
            create_obj = UserBonusQuery().create(
                user=user, bonus=data.bonus, amount_bonus=data.amount
            )
        return create_obj
