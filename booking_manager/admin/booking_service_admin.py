from django.contrib import admin

from booking_manager.models import BookingService

@admin.register(BookingService)
class BookingServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'price'
    ]
    search_fields = [
        'name',
        'description'
    ]