from django.contrib import admin


from .models import User, Client, Barber
from booking_manager.models import Comment

admin.site.register(User)
admin.site.register(Client)

class CommentInline(admin.TabularInline):
    model = Comment
    fields = [
        'client',
        'text',
        'rating',
        'is_published'
    ]
    extra = 0

@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = [
        'name_surname',
        'barbershop_work'
    ]
    inlines = [
        CommentInline
    ]

    @admin.display(description='Имя Барбера')
    def name_surname(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    @admin.display(description='Барбершоп')
    def barbershop_work(self, obj):
        return obj.barbershop
