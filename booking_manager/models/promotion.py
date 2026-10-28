from django.db import models

from core.models import DateTimeMixin

class Promotion(DateTimeMixin):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    discount_percent = models.PositiveSmallIntegerField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    services = models.ManyToManyField(
        to='BookingService',
        related_name='promotions',
        verbose_name='Услуги'
    )

    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'Promotion'
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ['-created_at']

    def __str__(self):
        return self.name