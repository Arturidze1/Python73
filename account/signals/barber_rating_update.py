from django.db.models import Avg
from django.dispatch import receiver
from django.db.models.signals import post_save

from account.models import Client
from booking_manager.models import Comment


@receiver(post_save, sender=Comment)
def barber_rating_update(sender, instance, created, **kwargs):
    barber = instance.barber

    avg_rating = Comment.objects.filter(barber=barber, is_published=True).aggregate(Avg('rating'))['rating__avg']

    barber.rating = avg_rating
    barber.save(update_fields=['rating'])

