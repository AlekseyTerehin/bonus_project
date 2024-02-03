from django.contrib.auth.models import User

from ...dto.bonus_dto import BonusDTO
from ...models import UserBonus


class AbstractSaversUserBonus:

    def save(self, data: BonusDTO, user: User) -> UserBonus:
        raise NotImplementedError
