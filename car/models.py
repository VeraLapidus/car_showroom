from django.db import models

from producer.models import Producer
from customer.models import Customer


class Car(models.Model):
    """ Класс автомобилей """

    name = models.CharField(max_length=200, blank=True, verbose_name="Бренд, модель, год автомобиля")
    color = models.CharField(max_length=200, blank=True, verbose_name="Цвет автомобиля")
    description = models.TextField(blank=True, verbose_name='Описание')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')


    class Meta:
        ordering = ['name']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.name


class CarInstance(models.Model):
    """ Класс экземпляра автомобиля """

    name = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")

    CONDITION = [('wish_auto_show', 'желаемый для автосалона'), ('wish_customer', 'желаемый для покупателя'),
                 ('in_showroom', 'в автосалоне'), ('at_producer', 'у производителя'), ('at_customer', 'у покупателя')]
    condition = models.CharField(max_length=40, choices=CONDITION, verbose_name='Статус авто')

    price = models.IntegerField(blank=True, verbose_name='Цена, USD')
    # discount = models.ForeignKey('Discount', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Акция")
    price_discount = models.IntegerField(blank=True, null=True, verbose_name='Цена со скидкой, USD')
    price_action = models.IntegerField(blank=True, null=True, verbose_name='Цена по акции, USD')


    producers = models.ForeignKey(Producer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Производитель')
    # auto_shows = models.ForeignKey(Auto_show, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автосалон')
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Покупатель')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')


    class Meta:
        ordering = ['name']
        verbose_name = 'Экземпляр автомобиля'
        verbose_name_plural = 'Экземпляры автомобиля'

    def __str__(self):
        return self.name
