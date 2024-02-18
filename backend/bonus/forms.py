from django import forms
from django.core.exceptions import ValidationError

from .models import Bonus


class BonusForm(forms.ModelForm):
    class Meta:
        model = Bonus
        fields = (
            'bonus_name',
            'is_limit',
            'amount_bonus',
        )

    def clean(self):
        cleaned_data = super().clean()
        limit = cleaned_data.get('is_limit')
        if limit:
            if not cleaned_data.get('amount_bonus'):
                raise ValidationError('Для лимитированного бонуса необходимо установить количество')
            return cleaned_data
        if cleaned_data.get('amount_bonus'):
            raise ValidationError('Для безлимитного бонуса количество бонусов необходимо оставить пустым')
        return cleaned_data
