from django.db import models


class Post(models.Model):
	"""Модель для новостных постов"""
	slug = models.SlugField(
		verbose_name='Уникальное название для URL',
		max_length=64,
		unique=True
	)
	title = models.CharField(
		verbose_name='Заголовок новости',
		max_length=256
	)
	body = models.TextField(
		verbose_name='Основной текст новости',
		max_length=8192
	)
	image = models.FileField(
		verbose_name='Картинка для новости',
		upload_to='news_images/'
	)
	date_creation = models.DateTimeField(
		verbose_name='Время создания поста',
		auto_now_add=True
	)
	objects = models.Manager()
