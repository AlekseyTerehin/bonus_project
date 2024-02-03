from itertools import groupby
from typing import List

from django.contrib.auth.models import User
from django.db.models import QuerySet

from users.dto.user_bonus_dto import UserBonusDTO


class UserQueries:

    def __init__(self):
        self.users = User.objects.all()

    def get_users(self):
        users_info = self.users.select_related('userbonus__bonus').values(
            'pk', 'date_joined', 'userbonus__bonus__bonus_name'
        ).order_by('pk')
        return self.__grouped_bonus(users_info=users_info)

    @staticmethod
    def __grouped_bonus(users_info: QuerySet[User]) -> List[UserBonusDTO]:
        group_users = groupby(users_info, key=lambda x: (x['pk'], x['date_joined']))
        users_list = []
        for group, rows in group_users:
            user_id, date_joined = group
            user_bonuses = UserBonusDTO(
                pk=user_id,
                date_joined=date_joined,
                bonuses=[row['userbonus__bonus__bonus_name'] for row in rows]
            )
            users_list.append(user_bonuses)
        return users_list
