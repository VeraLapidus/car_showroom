from django.db import models
from django_countries.fields import CountryField


class Producer(models.Model):
    """ Класс поставщиков """

    name = models.CharField(max_length=200, verbose_name="Название поставщика")
    country = CountryField(verbose_name="Страна")
    year_foundation = models.IntegerField(blank=True, verbose_name='Год основания')
    balance = models.IntegerField(default=0, verbose_name='Баланс поставщика, USD')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        ordering = ['name']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name
