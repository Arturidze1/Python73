from django.contrib import admin
from django.db.models import F

from booking_manager.models import Product


@admin.action(description='Увеличить выбранное количество товаров на 10')
def add_ten_products(modeladmin, request, queryset):
    queryset.update(amount = F('amount') + 10)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'amount'
    ]
    list_editable = [
        'price',
        'amount'
    ]
    search_fields = [
        'name'
    ]
    actions = [
        add_ten_products
    ]