from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	"""Расширенная модель пользователя"""
	team_control = models.OneToOneField(
		'teams.Team',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		verbose_name='Команда которую можно редактировать'
	)
