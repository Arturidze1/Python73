from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from booking_manager.models import Booking


@receiver(post_save, sender=Booking)
def client_status(sender, instance, **kwargs):
    client = instance.client

    book_cnt = client.bookings.filter(is_active=False).count()

    if book_cnt <= 2:
         client.status = 'Noob'

    elif 2 < book_cnt < 10:
         client.status = 'Beginner'

    elif 11 < book_cnt < 20:
         client.status = 'Expert'

    else:
         client.status = 'Legend'

    client.save(update_fields=['status'])

