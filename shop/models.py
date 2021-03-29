from django.db import models


class Product(models.Model):
	"""Модель списка товара(мерча)"""
	slug = models.SlugField(
		verbose_name='Уникальное название для URL',
		max_length=64,
		unique=True
	)
	name = models.CharField(
		verbose_name='Название товара',
		max_length=256
	)
	description = models.TextField(
		verbose_name='Характеристики/описание товара',
		max_length=256
	)
	url_shop = models.URLField(
		verbose_name='Ссылка на товар',
		max_length=256
	)
	price = models.PositiveIntegerField(
		verbose_name='Стоимость товара'
	)
	image = models.FileField(
		verbose_name='Картинка товара',
		upload_to='shop_images/'
	)
	date_creation = models.DateTimeField(
		verbose_name='Время создания товара',
		auto_now_add=True
	)
