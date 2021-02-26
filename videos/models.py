from django.db import models


class Video(models.Model):
	"""Модель для постов с видео"""
	slug = models.SlugField(
		verbose_name='Уникальное название для URL',
		max_length=64
	)
	name = models.CharField(
		verbose_name='Название видео',
		max_length=256
	)
	body = models.CharField(
		verbose_name='Краткое описание видео',
		max_length=1024
	)
	url_video = models.URLField(
		verbose_name='Ссылка на видео',
		max_length=256
	)
	date_creation = models.DateTimeField(
		verbose_name='Время создания поста с видео',
		auto_now_add=True
	)
