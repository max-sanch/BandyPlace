# Generated by Django 3.1.6 on 2021-02-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=64, verbose_name='Уникальное название для URL')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок новости')),
                ('body', models.CharField(max_length=4096, verbose_name='Основной текст новости')),
                ('image', models.FileField(upload_to='news_images/', verbose_name='Картинка для новости')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Время создания поста')),
            ],
        ),
    ]