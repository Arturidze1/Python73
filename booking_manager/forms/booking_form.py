from django.utils import timezone
from django import forms

from account.models import Barber
from booking_manager.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'visit_time', 'booking_service', 'barber']
        widgets = {
            'visit_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
        }

    def clean(self):
        clean_obj = super().clean()
        visit_time = clean_obj.get('visit_time')
        barber = clean_obj.get('barber')

        if visit_time and visit_time < timezone.now():
            self.add_error('visit_time', 'Время записи не может быть прошлым!')

        if visit_time and barber:

            check_busy = Booking.objects.filter(
                barber=barber,
                visit_time=visit_time,
                is_active=True
            ).exists()

            if check_busy:
                self.add_error('visit_time', 'Бронирование уже существует')

        return clean_obj



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['visit_time'].input_formats = ['%Y-%m-%dT%H:%M']

        self.fields['booking_service'].empty_label = '----Выберите услугу----'
        self.fields['barber'].empty_label = '----Выберите барбера----'

        self.fields['barber'].queryset = Barber.objects.select_related('user')