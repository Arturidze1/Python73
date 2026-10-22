from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BaseModel


class Comment(BaseModel):
    text = models.TextField(
        verbose_name='Текст комментария',
        null=True,
        blank=True
    )

    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5),
                    MinValueValidator(1)],
        verbose_name='Оценка'
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовать?'
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