# Generated by Django 3.1.6 on 2021-02-27 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1024, verbose_name='Характеристики/описание товара'),
        ),
    ]
