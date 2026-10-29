from django.db import models

from core.models import DateTimeMixin, RatingMixin



class Barber(DateTimeMixin, RatingMixin):

    experience = models.IntegerField(blank=True)
    user = models.OneToOneField(
        to='account.User',
        related_name='barber',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    barbershop = models.ForeignKey(
        to='booking_manager.Barbershop',
        related_name='barbers',
        on_delete=models.SET_NULL,
        null=True,
        blank=True

    )

    class Meta:
        ordering = ['-id', '-created_at']
        db_table = 'Barbers'
        verbose_name = 'Барбер'
        verbose_name_plural = 'Барберы'

    def __str__(self):
        return self.user.email