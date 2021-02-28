from django.db import models


class UpcomingGame(models.Model):
	"""Модель предстоящих игр"""
	team_one = models.ForeignKey(
		'teams.Team',
		related_name='ug_team_one',
		on_delete=models.CASCADE,
		verbose_name='Первая команда'
	)
	team_two = models.ForeignKey(
		'teams.Team',
		related_name='ug_team_two',
		on_delete=models.CASCADE,
		verbose_name='Вторая команда'
	)
	date = models.DateField(
		verbose_name='Дата проведения матча (дд.мм.гггг)'
	)
	time = models.TimeField(
		verbose_name='Время проведения матча (чч:мм)'
	)
	address = models.CharField(
		verbose_name='Место проведения матча',
		max_length=256
	)
	date_creation = models.DateTimeField(
		verbose_name='Время создания записи',
		auto_now_add=True
	)
