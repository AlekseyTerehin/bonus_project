from rest_framework import serializers

from ..models import Bonus


class SerializersBonus(serializers.ModelSerializer):

    class Meta:
        model = Bonus
        fields = ('bonus_name',)
