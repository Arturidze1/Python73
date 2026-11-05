from django import forms
from booking_manager.models import BookingService


class BookingServiceForm(forms.ModelForm):
    class Meta:
        model = BookingService
        fields = ['name', 'category', 'description', 'price', 'duration_minutes', 'is_active']
        widgets = {
            'description' : forms.Textarea(attrs={'style': 'resize: none'})
        }

    def clean(self):
        clean_obj = super().clean()
        duration_minutes = clean_obj.get('duration_minutes')
        price = clean_obj.get('price')

        if duration_minutes and duration_minutes <= 0:
            self.add_error('duration_minutes', 'Продолжительность услуги не может быть меньше или равна 0')

        if price and price < 0:
            self.add_error('price', 'Цена не может быть отрицательной')

        return clean_obj

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].label = 'Название услуги'
        self.fields['category'].label = 'Категория услуги'
        self.fields['description'].label = 'Описание услуги'
        self.fields['price'].label = 'Стоимость услуги'
        self.fields['duration_minutes'].label = 'Продолжительность услуги'
        self.fields['is_active'].label = 'Активность услуги'
