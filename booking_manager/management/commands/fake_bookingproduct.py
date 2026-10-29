import random

from django.core.management import BaseCommand
from booking_manager.models import Product, Booking


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        products = Product.objects.all()
        for book in Booking.objects.all():
            for _ in range(1, random.randint(1, 10)):
                book.products.add(random.choice(products))


        self.stdout.write(self.style.SUCCESS('Данные успешно сгенерированы!'))