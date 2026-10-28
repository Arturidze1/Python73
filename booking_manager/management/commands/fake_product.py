import random


from django.core.management import BaseCommand
from faker import Faker
from booking_manager.models import Product



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')


        products_types = [
            'Шампунь', 'Гель для волос', 'Воск для усов', 'Бальзам для бороды',
            'Помада для волос', 'Тоник для лица', 'Масло для бороды', 'Пудра для объема',
            'Лак для волос', 'Воск', 'Кондиционер', 'Термозащита', 'Крем для укладки',
            'Масло для волос', 'Скраб', 'Пилинг', 'Паста для волос', 'Солевой спрей', 'Гель для бритья'
        ]
        brands = ['BarberPro', 'OldSchool', 'ManCare', 'BeardGrow', 'StyleUp', 'ClassicCut', 'Head&Shoulders', 'Elseve',
                  'Belita', 'GlissKur', 'Mixit', 'Pantene', 'Garnier', 'Tashe', 'Shauma', 'Dove', 'LoReal', 'Matrix',
                  'Lador', 'Estel']
        products = []

        for _ in range(10):
            name = f"{random.choice(brands)} {random.choice(products_types)}"
            volume = random.choice(['50 мл','100 мл', '200 мл', '250 мл','300 мл', '400 мл', '500 мл'])
            full_name = f"{name} {volume}"

            Product.objects.create(
                name=full_name,
                description=fake.text(max_nb_chars=200),
                price=random.randint(15, 150),
                amount=random.randint(0, 50)
            )

            Product.objects.bulk_create(products)

        self.stdout.write(self.style.SUCCESS('Данные успешно сгенерированы!'))