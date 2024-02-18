from django.contrib.auth.models import User
from rest_framework import serializers


class CharListField(serializers.ListField):
    bonus_name = serializers.CharField()


class SerializersUsers(serializers.ModelSerializer):

    bonuses = CharListField()

    class Meta:
        model = User
        fields = ['pk', 'date_joined', 'bonuses']
