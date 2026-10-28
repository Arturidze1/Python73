from django.contrib import admin

from booking_manager.models import Barbershop, Booking, BookingService, Comment, Product, ProductBooking, Promotion


admin.site.register(Barbershop)
admin.site.register(Booking)
admin.site.register(BookingService)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(ProductBooking)
admin.site.register(Promotion)
