from booking_manager.models import Barbershop
from django.contrib import admin

@admin.register(Barbershop)
class BarbershopAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
        'phone',
        'description',
        'get_services'
    ]
    search_fields = [
        'name',
        'address'
    ]

    @admin.display(description='Барбершопы')
    def get_services(self, obj):
        services_lst = [str(service) for service in obj.services.all()]
        return ', '.join(services_lst)