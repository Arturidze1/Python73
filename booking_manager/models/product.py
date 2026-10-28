from django.db import models

from core.models import DateTimeMixin

class Product(DateTimeMixin):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()

    bookings = models.ManyToManyField(
        to='Booking',
        related_name='products',
        verbose_name='Бронирования',
        through='ProductBooking'
    )

    class Meta:
        db_table = 'Products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at','-price', '-amount']

    def __str__(self):
        return self.name
