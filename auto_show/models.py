from django.db import models
from django_countries.fields import CountryField


class Auto_show(models.Model):
    """ Класс автосалона """

    name = models.CharField(max_length=200, blank=True, verbose_name="Название автосалона")
    country = CountryField(blank=True, verbose_name="Страна")
    year_foundation = models.IntegerField(blank=True, verbose_name='Год основания')
    balance = models.IntegerField(default=0, verbose_name='Баланс автосалона, USD')
    wish_cars = models.CharField(max_length=500, blank=True, verbose_name="Автомобили к приобретению")
    list_producers = models.CharField(max_length=500, blank=True, verbose_name="Список поставщиков")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        ordering = ['name']
        verbose_name = 'Автосалон'
        verbose_name_plural = 'Автосалоны'

    def __str__(self):
        return self.name
