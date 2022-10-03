from django.db import models

from auto_show.models import Auto_show
from producer.models import Producer
from customer.models import Customer


class Car(models.Model):
    """Класс автомобилей"""

    short_name = models.CharField(max_length=200, verbose_name="Сокращенное название автомобиля (н-р, Audi Q5 2015")
    brand = models.CharField(max_length=200, verbose_name="Бренд автомобиля")
    model = models.CharField(max_length=200, verbose_name="Модель автомобиля")
    year_launch = models.IntegerField(blank=True, verbose_name='Год выпуска')

    amount = models.IntegerField(blank=True, verbose_name='Количество')
    description = models.TextField(blank=True, verbose_name='Описание')

    CONDITION = [('wish_auto_show', 'желаемый для автосалона'), ('wish_customer', 'желаемый для покупателя'),
                 ('in_showroom', 'в автосалоне'), ('at_producer', 'у производителя'), ('at_customer', 'у покупателя')]
    condition = models.CharField(max_length=40, choices=CONDITION, blank=True, null=True, verbose_name='Статус авто')

    price = models.IntegerField(blank=True, verbose_name='Цена, USD')
    # discount = models.ForeignKey('Discount', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Акция")
    price_discount = models.IntegerField(blank=True, null=True, verbose_name='Цена со скидкой, USD')
    price_action = models.IntegerField(blank=True, null=True, verbose_name='Цена по акции, USD')

    producers = models.ManyToManyField(Producer, verbose_name='Производитель')
    auto_shows = models.ManyToManyField(Auto_show, verbose_name='Автосалон')
    customers = models.ManyToManyField(Customer, verbose_name='Покупатель')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def short_name(self):
        """ Сокращенное название автомобиля"""

        short_name = self.brand + self.model + str(self.year_launch)
        return short_name



    class Meta:
        # ordering = ['short_name']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.short_name


