from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from ....dto.bonus_dto import BonusDTO
from ....models import Bonus, UserBonus
from ....services.savers_bonus.random_bonus_saver import RandomBonusSaver


class RandomBonusSaverTestCase(TestCase):

    def setUp(self):
        self.bonus_saver = RandomBonusSaver()

    def test_successful_save(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=1)
        dto = BonusDTO(bonus=bonus, amount=1)
        user = User.objects.create(username='Тестер1', password='123456')
        result = self.bonus_saver.save(data=dto, user=user)
        test_data = UserBonus.objects.get(user=user)
        self.assertEqual(test_data, result)

    def test_bonus_is_over(self):
        bonus = Bonus.objects.create(bonus_name='тестовый бонус1', is_limit=True, amount_bonus=0)
        dto = BonusDTO(bonus=bonus, amount=1)
        user = User.objects.create(username='Тестер1', password='123456')
        with self.assertRaises(ValueError):
            self.bonus_saver.save(data=dto, user=user)
        with self.assertRaises(ObjectDoesNotExist):
            UserBonus.objects.get(user=user)
