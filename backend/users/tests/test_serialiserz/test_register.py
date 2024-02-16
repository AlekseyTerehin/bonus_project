from django.contrib.auth.models import User
from django.test import TestCase

from users.serializers.register import RegisterUserSerializer


class RegisterUserSerializerTestCase(TestCase):

    def test_ok(self):
        result = RegisterUserSerializer(data={'username': 'Тестовый', 'password': '123456'})
        is_valid = result.is_valid()
        self.assertTrue(is_valid)
        save_user = result.save()
        expected_result = User.objects.get(username='Тестовый')
        self.assertEqual(expected_result, save_user)

    def test_already_user(self):
        User.objects.create(username='Тестовый', password='123456')
        result = RegisterUserSerializer(data={'username': 'Тестовый', 'password': '123456'})
        is_valid = result.is_valid()
        self.assertFalse(is_valid)
        with self.assertRaises(AssertionError):
            result.save()

    def test_small_len_username(self):
        result = RegisterUserSerializer(data={'username': 'Тест', 'password': '123456'})
        is_valid = result.is_valid()
        self.assertFalse(is_valid)
        with self.assertRaises(AssertionError):
            result.save()

    def test_large_len_username(self):
        result = RegisterUserSerializer(
            data={
                'username': 'ТестовыйТестТестеровичаТестирующийТестогоТестерантаТестинского',
                'password': '123456'
            }
        )
        is_valid = result.is_valid()
        self.assertFalse(is_valid)
        with self.assertRaises(AssertionError):
            result.save()
