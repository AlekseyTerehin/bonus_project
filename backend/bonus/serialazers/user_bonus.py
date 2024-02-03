from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import UserBonus


class SerializersUserBonus(serializers.ModelSerializer):
    user_pk = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True,
                                                 allow_null=True)

    class Meta:
        model = UserBonus
        fields = ('user_pk', 'bonus')
