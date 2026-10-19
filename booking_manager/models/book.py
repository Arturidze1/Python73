from django.db import models
from django.core.validators import MinValueValidator
from booking_manager.constants import CategoryChoices


class Booking(models.Model):

    name = models.CharField(
        max_length=30,
        verbose_name='Наименование',
        unique=True
    )

    description = models.TextField(
        max_length=255,
        verbose_name='Описание',
        null=True,
        blank=True
    )

    price = models.FloatField(
        verbose_name='Цена',
        validators=[MinValueValidator(0)]
    )

    category = models.CharField(
        choices=CategoryChoices,
        verbose_name='Категория',
        default=CategoryChoices.HAIRCUT
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookings'
        verbose_name = 'Бронирование мастера'
        ordering = ['-created_at','-price', 'category']

    def __str__(self):
        return self.name

