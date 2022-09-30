from django.db import models

class Car(models.Model):
    """Класс автомобилей"""

    short_name = models.CharField(max_length=200, verbose_name="Сокращенное название автомобиля (н-р, Audi Q5")
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

    producers = models.ManyToManyField('Producer', verbose_name='Производитель')
    auto_shows = models.ManyToManyField('Auto_show', verbose_name='Автосалон')
    customers = models.ManyToManyField('Customer', verbose_name='Покупатель')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Активен')


    # def get_price_discount(self):
    #     """Расчитать стоимость со скидкой"""
    #
    #     price = int(self.price * (100 - self.price_discount) / 100)
    #     return price


    class Meta:
        ordering = ['short_name']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.short_name



class DealList (models.Model):
    """Список совершенных сделок"""

    name = models.CharField(max_length=200, blank=True, verbose_name="Название сделки")

    PARTICIPANTS = [('producer-showroom', 'поставщик-автосалон'), ('showroom-customer', 'автосалон-покупатель')]
    participants = models.CharField(max_length=40, choices=PARTICIPANTS, verbose_name='Стороны сделки')
    price = models.IntegerField(verbose_name='Сумма сделки, USD')

    auto_shows = models.ForeignKey('Auto_show', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автосалон')
    producers = models.ForeignKey('Producer', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Продавец")
    customers = models.ForeignKey('Сustomer', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Покупатель')
    cars = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name='Авто')



    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата совершения сделки")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления сделки")

class Discount(models.Model):
    """ Скидка постоянного покупателя """

    name = models.CharField(max_length=50, verbose_name='Имя скидки')
    amount = models.IntegerField(verbose_name='Размер скидки %')
    date_start = models.DateTimeField(verbose_name='Дата начала скидки (dd.mm.yyyy 00:00:00)')
    date_finish = models.DateTimeField(verbose_name='Дата окончания скидки (dd.mm.yyyy 00:00:00)')

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
    amount = models.IntegerField(verbose_name='Размер скидки %')
    date_start = models.DateTimeField(verbose_name='Дата начала акции (dd.mm.yyyy 00:00:00)')
    date_finish = models.DateTimeField(verbose_name='Дата окончания акции (dd.mm.yyyy 00:00:00)')
    description = models.TextField(max_length=500, blank=True)

    cars = models.ManyToManyField('Car', verbose_name='Автомобиль')
    auto_shows = models.ManyToManyField('Auto_show', verbose_name='Автосалон')


    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['date_start']
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return self.name

