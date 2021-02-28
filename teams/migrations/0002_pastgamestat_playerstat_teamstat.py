# Generated by Django 3.1.6 on 2021-02-27 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team', verbose_name='Команда')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.player', verbose_name='Игрок')),
            ],
        ),
        migrations.CreateModel(
            name='PastGameStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('past_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.pastgame', verbose_name='Игра')),
            ],
        ),
    ]
