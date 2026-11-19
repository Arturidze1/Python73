from django.contrib import admin

from booking_manager.models import Booking, ProductBooking


class ProductBookingInline(admin.TabularInline):
    model = ProductBooking
    extra = 1

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'visit_time',
        'is_active',
        'get_barber_email',
        'get_client_email',
        'booking_service',
        'custom_barber_service',
        'created_at_field',
        'total_price_products'
        ]
    list_display_links = [
        'name',
        'visit_time'
    ]
    list_editable = [
        'is_active'
    ]
    readonly_fields = [
        'created_at_field',
        'total_price_products'
    ]
    inlines = [
        ProductBookingInline
    ]

    search_fields = [
        'client__user__email',
        'name',
        'barber__user__first_name'
    ]

    list_filter = [
        'is_active',
        'visit_time',
        'barber',
        'booking_service'
    ]

    @admin.display(description='Общая сумма товаров')
    def total_price_products(self, obj):
        items = obj.products_to_book.all()
        total_price = 0
        for item in items:
            total_price += item.total_price
        return f'{total_price} BYN'

    @admin.display(description='Бронирование создано')
    def created_at_field(self, obj):
        return obj.created_at

    @admin.display(empty_value='Без email', description='Email Барбера')
    def get_barber_email(self, obj)  :
        if obj.barber:
            return obj.barber.user.email
        return 'Отсутствует барбер'

    @admin.display(empty_value='Без email', description='Email Клиента')
    def get_client_email(self, obj):
        if obj.client:
            return obj.client.user.email
        return 'Отсутствует клиент'

    @admin.display(description='Имя Барбера - Услуга')
    def custom_barber_service(self, obj):
        if obj.barber:
            return f'{obj.barber.user.first_name} - {obj.booking_service}'
        return f'Барбер отсутствует - {obj.booking_service}'