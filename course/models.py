from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    image = models.ImageField(upload_to='course/', verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='lesson/', verbose_name='Изображение', **NULLABLE)
    url = models.URLField(verbose_name='Cсылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
