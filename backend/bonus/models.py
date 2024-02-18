from django.contrib.auth.models import User
from django.db import models


class UserBonus(models.Model):

    user = models.ForeignKey(User, related_name='userbonus', on_delete=models.CASCADE)
    bonus = models.ForeignKey('Bonus', related_name='bonus', on_delete=models.CASCADE)
    amount = models.IntegerField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.bonus}'

    class Meta:
        verbose_name = 'Пользовательский_бонус'
        verbose_name_plural = 'Пользовательские_бонусы'


class Bonus(models.Model):

    bonus_name = models.CharField(max_length=100, unique=True)
    is_limit = models.BooleanField(default=True)
    amount_bonus = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.bonus_name

    class Meta:
        verbose_name = 'Бонус'
        verbose_name_plural = 'Бонусы'
