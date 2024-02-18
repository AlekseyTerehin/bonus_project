from django.contrib.auth.models import User
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import QuerySet


class UserQueries:

    def __init__(self):
        self.users = User.objects.all()

    def get_users(self) -> QuerySet[User]:
        return (
            self.users.values('pk', 'date_joined')
            .annotate(bonuses=ArrayAgg('userbonus__bonus__bonus_name'))
            .order_by('pk')
        )
