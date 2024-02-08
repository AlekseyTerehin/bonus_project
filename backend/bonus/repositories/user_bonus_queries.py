from django.contrib.auth.models import User
from django.db.models import QuerySet

from ..models import UserBonus, Bonus


class UserBonusQuery:

    def __init__(self):
        self.user_bonus_objects: QuerySet[UserBonus] = UserBonus.objects.all()

    def create(self, user: User, bonus: Bonus, amount_bonus: int) -> UserBonus:
        if amount_bonus <= 0:
            raise ValueError('Аттрибут amount_bonus должен быть больше нуля')

        return self.user_bonus_objects.create(user=user, bonus=bonus, amount=amount_bonus)

    def check_user_bonus(self, user: User) -> bool:
        return bool(self.user_bonus_objects.filter(user=user))
