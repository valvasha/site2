# Generated by Django 5.0.4 on 2024-04-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0002_alter_abcmodel_a_alter_abcmodel_h_alter_abcmodel_m_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abcmodel',
            name='tusk',
            field=models.TextField(default='\n                Имеются две емкости: кубическая с ребром A, \n                цилиндрическая с высотой H и радиусом основания R. \n                Определить, можно ли заполнить жидкостью объёма \n                M первую емкость, вторую, обе.\n                ', max_length=255, verbose_name='Формулировка задачи'),
        ),
    ]