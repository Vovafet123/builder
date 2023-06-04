from django.db import models, transaction
from django.db.models import Q


class TransportStatus(models.TextChoices):
    WAIT = ('WAIT', 'Ожидает')
    IN_TRANSIT = ('IN_TRANSIT', 'В пути')
    RETURN = ('RETURN', 'Возвращается')


class FlightStatus(models.TextChoices):
    FREE = ('FREE', 'FREE')
    PLAN = ('PLAN', 'PLAN')
    CANCELED = ('CANCELED', 'CANCELED')
    IN_ROAD = ('IN_ROAD', 'IN_ROAD')
    DONE = ('DONE', 'DONE')


class Transport(models.Model):
    model = models.CharField("Модель", max_length=100)
    number_and_region = models.CharField("Номер и регион", max_length=9, unique=True)
    max_load_capacity = models.PositiveSmallIntegerField("Максимальный вес")
    max_loading_volume = models.PositiveSmallIntegerField("Максимальный объем")
    status = models.CharField("Статус", max_length=255, choices=TransportStatus.choices)
    place = models.CharField("Место", max_length=255)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(max_load_capacity__range=(1, 40)), name='max_load_capacity_constraint'),
            models.CheckConstraint(check=Q(max_loading_volume__range=(5, 150)), name='max_loading_volume_constraint'),
        ]

        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"


class Product(models.Model):
    name = models.CharField("Наименование", max_length=255)
    manufacturer = models.CharField("Производитель", max_length=255)  # Производитель
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.manufacturer}'

    class Meta:
        models.CheckConstraint(check=Q(price__gte=0.00), name='price_constraint')
        
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Stock(models.Model):
    city = models.CharField("Город", max_length=255)
    address = models.CharField("Адрес", max_length=255)
    free_volume = models.PositiveSmallIntegerField("свободный объем")
    products = models.ManyToManyField(Product, through='StockProduct')
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.city}, {self.address}'

    class Meta:
        unique_together = ('city', 'address',)

        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class Flight(models.Model):
    source = models.CharField("Город отправки", max_length=255)  # Город отправки
    destination = models.CharField("Город доставки", max_length=255)  # Город доставки
    status = models.CharField("Статус", max_length=255, choices=FlightStatus.choices, default=FlightStatus.FREE, blank=True)
    revenue = models.DecimalField("Выручка", max_digits=10, decimal_places=2)  # Выручка
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        models.CheckConstraint(check=Q(revenue__gte=0.00), name='revenue_constraint')

        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"

    # def save(self, *args, **kwargs):
    #     with transaction.atomic():
    #         super().save(*args, **kwargs)




class StockProduct(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('product', 'stock',)

        verbose_name = "Склад и товары"
        verbose_name_plural = "Склады и товары"
