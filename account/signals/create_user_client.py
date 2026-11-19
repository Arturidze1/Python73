from django.dispatch import receiver
from django.db.models.signals import post_save


from django.contrib.auth import get_user_model

from account.models import Client


@receiver(post_save, sender=get_user_model())
def create_user_client(sender, instance, created, **kwargs):
    if created:
        client = Client.objects.get_or_create(user=instance)
        print(f'Клиент создан - {client.user.first_name}')
    else:
        print(f'Пользователь обновлен - {instance.first_name}')