# Generated by Django 5.0.4 on 2024-05-02 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название страницы')),
                ('url', models.CharField(max_length=10, verbose_name='Уникальный url')),
                ('nav_title', models.CharField(max_length=20, verbose_name='Заголовок в навигации')),
                ('content', models.TextField(verbose_name='Контент')),
                ('nav_position', models.IntegerField(verbose_name='Порядковый номер в навигации')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2024, 5, 2, 14, 47, 43, 335116))),
            ],
        ),
    ]