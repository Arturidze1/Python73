from django.db import models

from account.constants import ClientStatusChoices
from core.models import DateTimeMixin

class Client(DateTimeMixin):

    status = models.CharField(
        choices=ClientStatusChoices,
        default=ClientStatusChoices.NOOB)

    date_of_birth = models.DateField(null=True)
    user = models.OneToOneField(
        to='account.User',
        related_name='client',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-id', '-created_at']
        db_table = 'Clients'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


    def __str__(self):
        return self.user.email