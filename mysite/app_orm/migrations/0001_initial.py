# Generated by Django 5.0.4 on 2024-04-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbcModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tusk', models.CharField(default='\n                Имеются две емкости: кубическая с ребром A, \n                цилиндрическая с высотой H и радиусом основания R. \n                Определить, можно ли заполнить жидкостью объёма \n                M первую емкость, вторую, обе.\n                ', max_length=255, verbose_name='Формулировка задачи')),
                ('a', models.FloatField(verbose_name='Ребро A')),
                ('h', models.FloatField(verbose_name='Высота H')),
                ('r', models.FloatField(verbose_name='Радиус основания R')),
                ('m', models.FloatField(verbose_name='Объём жидкости M')),
            ],
        ),
    ]
