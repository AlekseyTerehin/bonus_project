from django.contrib import admin

from .forms import BonusForm
from .models import Bonus, UserBonus


@admin.register(Bonus)
class BonusAdm(admin.ModelAdmin):
    form = BonusForm
    model = Bonus
    fields = (
        'bonus_name',
        'is_limit',
        'amount_bonus',
    )
    list_display = (
        'bonus_name',
        'is_limit',
        'amount_bonus',
    )
    list_filter = ('is_limit',)


@admin.register(UserBonus)
class UserBonusAdm(admin.ModelAdmin):
    model = UserBonus
    fields = (
        'user',
        'bonus',
    )
    list_display = (
        'user',
        'bonus',
    )
