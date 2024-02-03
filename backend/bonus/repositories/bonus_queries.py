from django.db.models import Q, QuerySet

from ..models import Bonus


class BonusQuery:

    def __init__(self):
        self.bonus_objects = Bonus.objects.all()

    def get_active_bonuses(self) -> QuerySet[Bonus]:
        return self.bonus_objects.filter(Q(limit=False) | Q(amount_bonus__gt=0))

    @staticmethod
    def reduce(bonus: Bonus, amount_reduce: int) -> None:

        if amount_reduce <= 0:
            raise ValueError('Аттрибут amount_reduce должен быть больше нуля')

        if not bonus.limit:
            return

        if bonus.amount_bonus - amount_reduce < 0:
            raise ValueError('бонус закончился')

        bonus.amount_bonus -= amount_reduce
        bonus.save()
