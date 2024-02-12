# Generated by Django 4.2.9 on 2024-02-12 23:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bonus', '0002_rename_limit_bonus_is_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='bonus_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='userbonus',
            unique_together={('user', 'bonus')},
        ),
    ]
