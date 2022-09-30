from django.db import models


class Customer(models.Model):
    """ Класс покупателя """

    first_name = models.CharField(max_length=200, verbose_name="Имя покупателя")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия покупателя")
    full_name = models.CharField(max_length=400, verbose_name="Фамилия и имя покупателя")
    year_of_birth = models.IntegerField(blank=True, verbose_name='Год рождения')
    balance = models.IntegerField(default=0, verbose_name='Баланс покупателя, USD')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def full_name(self):
        """ Фамилия и имя покупателя"""

        full_name = self.last_name+self.first_name
        return full_name


    class Meta:
        ordering = ['full_name']
        verbose_name = 'ФИ покупателя'
        verbose_name_plural = 'ФИ покупателей'

    def __str__(self):
        return self.full_name

