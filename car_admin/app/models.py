from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django.conf import settings

class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name='Модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        rew_count = Review.objects.filter(car=self).count()
        return rew_count

    review_count.short_description = 'Количество статей'

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = RichTextField(config_name='default', verbose_name='Текст')

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        ordering = ['-car']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
