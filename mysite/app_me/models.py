from django.db import models
from datetime import datetime

# Create your models here.


class Content(models.Model):
    # Название страницы (title)
    title = models.CharField(
        max_length=50,
        verbose_name='Название страницы',
        default='Название страницы'
    )
    # Уникальный url
    url = models.CharField(
        max_length=10,
        verbose_name='Уникальный url',
        default='me/<url>'
    )
    # Заголовок в навигации
    nav_title = models.CharField(
        max_length=30,
        verbose_name='Заголовок в навигации',
        default='Заголовок в навигации'
    )
    # Контент на странице
    content = models.TextField(
        verbose_name='Контент',
        default='html код страницы, добавляется в блок content базового шаблона (app_me/templates/app_me/base.html)'
    )
    # Положение в навигации, определяется как порядковый номер.
    nav_position = models.IntegerField(
        verbose_name='Порядковый номер в навигации',
        default=1
    )
    # Дата изменения
    datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        pass

    @property
    def content_views_short(self) -> str:
        if len(self.content) < 30:
            return self.content
        return self.content[:30] + '...'

    def __str__(self) -> str:
        return f'{self.title}: url - /me/{self.url}'
