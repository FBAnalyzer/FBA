# Generated by Django 4.0.5 on 2022-07-06 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_level_remove_team_goalsgame_remove_team_goalsperiod_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Line',
        ),
    ]
