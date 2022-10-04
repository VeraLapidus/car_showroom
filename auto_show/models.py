from django.db import models
from django_countries.fields import CountryField

from car.models import Car


class Auto_show(models.Model):
    """ Класс автосалона """

    name = models.CharField(max_length=200, verbose_name="Название автосалона")
    country = CountryField(verbose_name="Страна")
    year_foundation = models.IntegerField(blank=True, verbose_name='Год основания')
    balance = models.IntegerField(default=0, verbose_name='Баланс автосалона, USD')
    wish_cars = models.ManyToManyField(Car, verbose_name="Автомобили к приобретению")

    list_auto = models.CharField(max_length=1500, blank=True, verbose_name="Список автомобилей салона")
    # можно вытащить по связям Auto_show -mtm- Car -fg- CarInstance #

    list_producers = models.CharField(max_length=1500, blank=True, verbose_name="Список поставщиков")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        ordering = ['name']
        verbose_name = 'Автосалон'
        verbose_name_plural = 'Автосалоны'

    def __str__(self):
        return self.name
