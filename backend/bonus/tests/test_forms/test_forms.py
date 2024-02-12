from django.test import TestCase

from ...forms import BonusForm
from ...models import Bonus


class BonusFormTestCase(TestCase):

    def test_ok(self):
        form_data_1 = {
            'bonus_name': 'Тестовый бонус 1',
            'is_limit': True,
            'amount_bonus': 10
        }
        form_data_2 = {
            'bonus_name': 'Тестовый бонус 2',
            'is_limit': False
        }

        form = BonusForm(data=form_data_1)
        self.assertTrue(form.is_valid())
        form.save()

        form = BonusForm(data=form_data_2)
        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(Bonus.objects.count(), 2)

    def test_unlimited_with_amount(self):
        form_data = {
            'bonus_name': 'Тестовый бонус',
            'is_limit': False,
            'amount_bonus': 10
        }
        form = BonusForm(data=form_data)
        self.assertFalse(form.is_valid())
        with self.assertRaises(ValueError):
            form.save()

    def test_limited_with_no_amount(self):
        form_data = {
            'bonus_name': 'Тестовый бонус',
            'is_limit': True
        }
        form = BonusForm(data=form_data)
        self.assertFalse(form.is_valid())
        with self.assertRaises(ValueError):
            form.save()
