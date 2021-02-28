from django.db import models


class Team(models.Model):
	"""Модель команды хоккея с мячом"""
	name = models.CharField(
		verbose_name='Название команды',
		max_length=128
	)
	logo = models.FileField(
		verbose_name='Логотип команды',
		upload_to='team_logos/'
	)
	date_creation = models.DateTimeField(
		verbose_name='Время создания команды',
		auto_now_add=True
	)

	def __str__(self):
		return self.name


class TeamStat(models.Model):
	"""Модель статистики команды хоккея с мячом"""
	team = models.ForeignKey(
		Team,
		on_delete=models.CASCADE,
		verbose_name='Команда'
	)


class Player(models.Model):
	"""Модель игроков хоккея с мячом"""
	full_name = models.CharField(
		verbose_name='ФИО игрока',
		max_length=256
	)
	team = models.ForeignKey(
		Team,
		on_delete=models.CASCADE,
		verbose_name='Команда в которой состоит игрок'
	)
	photo = models.FileField(
		verbose_name='Фото игрока',
		upload_to='player_photos/'
	)
	date_creation = models.DateTimeField(
		verbose_name='Время создания игрока',
		auto_now_add=True
	)

	def __str__(self):
		return self.full_name


class PlayerStat(models.Model):
	"""Модель статистики игроков хоккея с мячом"""
	player = models.ForeignKey(
		Player,
		on_delete=models.CASCADE,
		verbose_name='Игрок'
	)


class PastGame(models.Model):
	"""Модель прошедших игр"""
	team_one = models.ForeignKey(
		Team,
		related_name='pg_team_one',
		on_delete=models.CASCADE,
		verbose_name='Первая команда'
	)
	team_two = models.ForeignKey(
		Team,
		related_name='pg_team_two',
		on_delete=models.CASCADE,
		verbose_name='Вторая команда'
	)
	date = models.DateField(
		verbose_name='Дата проведения матча'
	)
	result = models.CharField(
		verbose_name='Результат матча',
		max_length=10
	)
	date_creation = models.DateTimeField(
		verbose_name='Время создания записи',
		auto_now_add=True
	)


class PastGameStat(models.Model):
	"""Модель статистики прошедших игр"""
	past_game = models.ForeignKey(
		PastGame,
		on_delete=models.CASCADE,
		verbose_name='Игра'
	)
