from datetime import timedelta
from django.utils import timezone
from random import choice,randint, randrange, sample


from django.core.management import BaseCommand
from booking_manager.models import *
from account.models import *
from faker import Faker
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Генерация данных'))
        fake = Faker('ru_RU')

        # Фейк услуги
        services_lst = []
        category_choices = ['Massage', 'Moustache', 'Beard', 'Haircut']
        for _ in range(20):

            services_lst.append(BookingService(
                category=choice(category_choices),
                name=fake.text(max_nb_chars=20),
                description=fake.text(max_nb_chars=200),
                price=randint(20,100),
                duration_minutes=randrange(10, 91, 10)
            ))

        BookingService.objects.bulk_create(services_lst)
        all_booking_service = list(BookingService.objects.all())

        # Фейк Барбершопы
        barbershops_lst = []
        for _ in range(5):

           barbershops_lst.append(Barbershop(
                name=fake.unique.company(),
                address=fake.unique.address(),
                phone=fake.unique.phone_number(),
                description=fake.text(max_nb_chars=200),
                ))

        Barbershop.objects.bulk_create(barbershops_lst)
        all_barbershops = list(Barbershop.objects.all())

        # Связь Услуги - Барбершоп
        for barbershop in all_barbershops:
            barbershop.services.set(sample(all_booking_service, randint(3,  10)))

        # Фейк Юзеры
        users_before = User.objects.count()
        users_lst = []
        for _ in range(100):

            users_lst.append(User(
                phone=fake.unique.phone_number(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                password=make_password(fake.password())
            ))

        User.objects.bulk_create(users_lst)
        all_users = list(User.objects.all()[users_before:])

        # Фейк Барберы
        barbers_lst = []
        for i in range(16):

            barbers_lst.append(Barber(
                experience=randint(1, 10),
                user=all_users[i],
                barbershop=choice(all_barbershops)
            ))

        Barber.objects.bulk_create(barbers_lst)
        all_barbers = list(Barber.objects.all())

        # Фейк Клиенты
        clients_lst = []
        for i in range(16, 81):

            clients_lst.append(Client(
                date_of_birth=fake.date_of_birth(minimum_age=14, maximum_age=80),
                user=all_users[i]
            ))

        Client.objects.bulk_create(clients_lst)
        all_clients = list(Client.objects.all())

        # Фейк Продукты
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

        for _ in range(50):
            name = f"{choice(brands)} {choice(products_types)}"
            volume = choice(['50 мл', '100 мл', '200 мл', '250 мл', '300 мл', '400 мл', '500 мл'])
            full_name = f"{name} {volume}"

            products.append(Product(
                name=full_name,
                description=fake.text(max_nb_chars=200),
                price=randint(15, 150),
                amount=randint(0, 50)
            ))

        Product.objects.bulk_create(products)
        all_products = list(Product.objects.all())

        # Фейк Бронь
        bookings_lst = []

        for _ in range(500):
            random_days = randint(-30, 30)
            random_hour = randint(9, 20)
            random_minutes = choice([0, 15, 30, 45])
            visit_time = timezone.now() + timedelta(
                days=random_days
            )
            visit_time = visit_time.replace(
                hour=random_hour,
                minute=random_minutes
            )

            bookings_lst.append(Booking(
                name=f"Бронирование {visit_time.strftime('%d.%m %H:%M')}",
                visit_time=visit_time,
                booking_service=choice(all_booking_service),
                barber=choice(all_barbers),
                client=choice(all_clients)
            ))

        Booking.objects.bulk_create(bookings_lst)
        all_bookings = list(Booking.objects.all())

        # Связь Продукты - Брони

        productsbookings_lst = []

        for _ in range(250):

            random_book = choice(all_bookings)
            random_product = choice(all_products)
            random_quantity = randint(1, 10)

            productsbookings_lst.append(ProductBooking(
                product=random_product,
                booking=random_book,
                quantity=random_quantity,
                total_price=random_quantity * random_product.price
            ))

        ProductBooking.objects.bulk_create(productsbookings_lst)

        # Фейк Комментарии

        comments_lst = []
        random_bookings = sample(all_bookings, 200)

        for random_book in random_bookings:

            comments_lst.append(Comment(
                text=fake.text(max_nb_chars=150),
                rating=randint(1, 5),
                is_published=choice([True, False]),
                booking=random_book,
                client=random_book.client,
                barber=random_book.barber

            ))

        Comment.objects.bulk_create(comments_lst)

        # Фейк Акции
        promotion_lst = []

        for _ in range(10):

            promotion_lst.append(Promotion(
                name=fake.text(max_nb_chars=20),
                description=fake.text(max_nb_chars=200),
                discount_percent=randint(1, 10),
                start_date=timezone.now().date(),
                end_date=(timezone.now() + timedelta(days=randint(10, 30))).date(),
            ))

        Promotion.objects.bulk_create(promotion_lst)
        all_promotions = list(Promotion.objects.all())

        # Связь Акции - Услуги

        for promo in all_promotions:
            random_service = sample(all_booking_service, randint(1, 3))
            promo.services.set(random_service)



        self.stdout.write(self.style.SUCCESS('Данные успешно сгенерированы!'))