from django.db import models

from booking_manager.constants import CategoryChoices
from core.models import DateTimeMixin

class BookingService(DateTimeMixin):

    category = models.CharField(
        max_length=20,
        choices=CategoryChoices,
        default=CategoryChoices.HAIRCUT,
    )
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, blank=True)
    price = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Booking_services'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-created_at','-price', 'category']

    def __str__(self):
        return self.name
