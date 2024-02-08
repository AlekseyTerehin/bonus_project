from django.contrib.auth.models import User

from .user_bonus_validator import UserBonusValidator


class RandonBonusValidator(UserBonusValidator):

    def is_valid(self, user: User) -> bool:
        is_user_bonus = self.queryset.check_user_bonus(user=user)
        return not is_user_bonus

    def get_message_error(self) -> str:
        return 'У пользователя уже есть бонус'
