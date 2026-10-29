from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import DateTimeMixin, RatingMixin



class Comment(DateTimeMixin, RatingMixin):
    text = models.TextField(
        verbose_name='Текст комментария',
        null=True,
        blank=True
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name='Публикация комментария'
    )

    client = models.ForeignKey(
        to='account.Client',
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Клиент'
    )

    barber = models.ForeignKey(
        to='account.Barber',
        related_name='received_comment',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Барбер'
    )

    booking = models.OneToOneField(
        to='Booking',
        related_name='comment',
        on_delete=models.CASCADE,
        verbose_name='Бронирование'
    )

    class Meta:
        db_table = 'Comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at', 'client']


    def __str__(self):
        client_email = self.client.user.email
        barber_email = self.barber.user.email
        return f'{client_email} -> {barber_email} rating {self.rating} '