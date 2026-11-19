from django.db import models

from core.models import DateTimeMixin

class Promotion(DateTimeMixin):

    name = models.CharField(max_length=100, verbose_name='Название акции')
    description = models.TextField(blank=True, verbose_name='Описание акции')
    discount_percent = models.PositiveSmallIntegerField(verbose_name='Скидка по акции')
    start_date = models.DateField(null=True, verbose_name='Дата начала акции')
    end_date = models.DateField(null=True, verbose_name='Дата окончания акции')

    services = models.ManyToManyField(
        to='BookingService',
        related_name='promotions',
        verbose_name='Услуги'
    )

    is_active = models.BooleanField(default=False, verbose_name='Активна ли акция')

    class Meta:
        db_table = 'Promotion'
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ['-created_at']

    def __str__(self):
        return self.name