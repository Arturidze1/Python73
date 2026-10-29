from django.contrib import admin
from booking_manager.models import Promotion

@admin.action(description='Активировать выбранные акции')
def activated_promotion(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description='Деактивировать выбранные акции')
def deactivated_promotion(modeladmin, request, queryset):
    queryset.update(is_active=False)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'discount_percent',
        'start_date',
        'end_date',
        'is_active',
        'get_name_of_service'
    ]

    @admin.display(description='Услуги на которые распространяется акция')
    def get_name_of_service(self, obj):
        if obj.services.exists():
            services_lst = [str(service) for service in obj.services.all()]
            return ','.join(services_lst)
        return 'Пока никуда не распространяется'

    actions = [
        activated_promotion,
        deactivated_promotion
    ]

