from django.db import models

from auto_show.models import Auto_show
from car.models import Car
from customer.models import Customer
from producer.models import Producer


class Deal(models.Model):
    """ Сделки """

    name = models.CharField(max_length=200, blank=True, verbose_name="Название сделки")

    PARTICIPANTS = [('producer-showroom', 'поставщик-автосалон'), ('showroom-customer', 'автосалон-покупатель')]
    participants = models.CharField(max_length=40, choices=PARTICIPANTS, verbose_name='Стороны сделки')
    price = models.IntegerField(verbose_name='Сумма сделки, USD')

    auto_shows = models.ForeignKey(Auto_show, on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name='Автосалон')
    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Продавец")
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name='Покупатель')
    cars = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Авто')

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата совершения сделки")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления сделки")

    class Meta:
        ordering = ['name']
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self):
        return self.name



class Discount(models.Model):
    """ Скидка постоянного покупателя """

    name = models.CharField(max_length=50, verbose_name='Имя скидки')
    amount_discount = models.IntegerField(verbose_name='Размер скидки в %')
    date_start = models.DateTimeField(verbose_name='Дата начала скидки (dd.mm.yyyy 00:00:00)')
    date_finish = models.DateTimeField(verbose_name='Дата окончания скидки (dd.mm.yyyy 00:00:00)')
    description = models.TextField(max_length=500, blank=True)

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['date_start']
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return self.name



class Action(models.Model):
    """ Акция """

    name = models.CharField(max_length=50, verbose_name='Имя акции')
    amount_action = models.IntegerField(verbose_name='Размер скидки по акции в %')
    date_start = models.DateTimeField(verbose_name='Дата начала акции (dd.mm.yyyy 00:00:00)')
    date_finish = models.DateTimeField(verbose_name='Дата окончания акции (dd.mm.yyyy 00:00:00)')
    description = models.TextField(max_length=500, blank=True)

    cars = models.ManyToManyField(Car, verbose_name='Автомобиль')
    auto_shows = models.ManyToManyField(Auto_show, verbose_name='Автосалон')
    producers = models.ManyToManyField(Producer, verbose_name='Поставщик')

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['date_start']
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name

