from math import pi
from django.db import models
import datetime

# Create your models here.

# Имеются две емкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R. Определить, можно ли заполнить жидкостью объёма M первую емкость, вторую, обе.
# class Form(forms.Form):
#     a = forms.FloatField(label="Ребро кубической ёмкости = ")
#     h = forms.FloatField(label="Высота цилиндрической ёмкости = ")
#     r = forms.FloatField(label="Радиус основания R = ")
#     m = forms.FloatField(label="Объём жидкости = ")


class AbcModel(models.Model):
    class Meta:
        pass
    # Формулировка задачи
    tusk = models.TextField(
        verbose_name='Формулировка задачи',
        default='Имеются две емкости: кубическая с ребром A, '
                'цилиндрическая с высотой H и радиусом основания R. '
                'Определить, можно ли заполнить жидкостью объёма '
                'M первую емкость, вторую, обе.',
        max_length=255,
    )
    # Переменные
    a = models.FloatField(
        verbose_name='Ребро A',
        default=0,
    )
    h = models.FloatField(
        verbose_name='Высота H',
        default=0,
    )
    r = models.FloatField(
        verbose_name='Радиус основания R',
        default=0,
    )
    m = models.FloatField(
        verbose_name='Объём жидкости M',
        default=0
    )
    result = models.CharField(
        verbose_name='Результат',
        default='Результат не определён',
        max_length=255,
    )
    # Дата-время
    datetime = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name='Дата и время создания'
    )

    def get_result(self):
        # Объём кубической ёмкости
        v_cube = self.a ** 2
        # Объём цилиндрической ёмкости
        v_cylinder = round(pi * (self.r ** 2) * self.h, 2)
        if self.m <= v_cube and self.m <= v_cylinder:
            return 'Жидкостью объёмом {} можно заполнить обе ёмкости.'.format(self.m)
        if self.m <= v_cube:
            return 'Жидкостью объёмом {} можно заполнить кубическую ёмкость.'.format(self.m)
        if self.m <= v_cylinder:
            return 'Жидкостью объёмом {} Можно заполнить цилиндрическую ёмкость.'.format(self.m)
        return 'Жидкостью объёмом {} нельзя заполнить ни одну из ёмкостей.'.format(self.m)
