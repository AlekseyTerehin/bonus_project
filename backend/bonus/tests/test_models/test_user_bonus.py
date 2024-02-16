from unittest import TestCase

from django.contrib.auth.models import User

from bonus.models import UserBonus, Bonus


class UserBonusModelTestCase(TestCase):

    def test_name_obj(self):
        user = User.objects.create(username='Тестер', password='123456')
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        userbonus = UserBonus.objects.create(user=user, bonus=bonus, amount=1)
        self.assertEqual('Тестер - тестовый бонус1', userbonus.__str__())
