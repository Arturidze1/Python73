from django.shortcuts import render
from booking_manager.models import Booking


def bookings(request):

    template_name = 'bookings.html'
    context = {
        'bookings': Booking.objects
        .select_related(
            'client__user',
            'barber__user',
            'booking_service'
        )
    }
    return render(request, template_name=template_name, context=context)
