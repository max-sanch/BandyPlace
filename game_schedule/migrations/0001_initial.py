# Generated by Django 3.1.6 on 2021-02-26 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Время проведения матча')),
                ('address', models.CharField(max_length=256, verbose_name='Место проведения матча')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')),
                ('team_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ug_team_one', to='teams.team', verbose_name='Первая команда')),
                ('team_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ug_team_two', to='teams.team', verbose_name='Вторая команда')),
            ],
        ),
    ]
