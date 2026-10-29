import datetime

from django.db import models

from core.models import DateTimeMixin

class Barbershop(DateTimeMixin):

    name = models.CharField(
        max_length=255,
        verbose_name='Филиал',
        unique=True
    )

    address = models.CharField(
        max_length=255,
        verbose_name='Адрес филиала',
        unique=True
    )

    phone = models.CharField(
        max_length=20,
        verbose_name='Контактный телефон',
        unique=True
    )

    description = models.TextField(verbose_name='Описание филиала', null=True, blank=True)

    opening_time = models.TimeField(verbose_name='Время открытия', default=datetime.time(9, 0))
    closing_time = models.TimeField(verbose_name='Время закрытия', default=datetime.time(22, 0))

    is_active = models.BooleanField(verbose_name='Работает ли филиал', default=True)

    services = models.ManyToManyField(
        to='BookingService',
        related_name='barbershops',
        verbose_name='Услуги',
    )

    class Meta:
        ordering = ['name', 'is_active']
        db_table = 'Barbershops'
        verbose_name = 'Барбершоп'
        verbose_name_plural = 'Барбершопы'

    def __str__(self):
        return self.name