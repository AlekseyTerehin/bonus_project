# Generated by Django 4.2.9 on 2024-02-13 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0003_alter_bonus_bonus_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userbonus',
            unique_together=set(),
        ),
    ]
