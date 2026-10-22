from django.db import models

from core.models import BaseModel

class Booking(BaseModel):

    name = models.CharField(
        max_length=30,
        verbose_name='Наименование',
        unique=True
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Активна'
    )

    visit_time = models.DateTimeField(
        verbose_name='Время визита',
        null=True,
        blank=True
    )

    booking_service = models.ForeignKey(
        to='BookingService',
        on_delete=models.SET_NULL,
        related_name='bookings',
        verbose_name='Услуга',
        null=True,
        blank=True
    )

    barber = models.ForeignKey(
        to='account.Barber',
        related_name='bookings',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )

    client = models.ForeignKey(
        to='account.Client',
        related_name='bookings',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )



    class Meta:
        db_table = 'Bookings'
        verbose_name = 'Бронирование мастера'
        verbose_name_plural = 'Бронирование мастеров'
        ordering = ['-created_at', 'name']

    def __str__(self):
        return self.name

