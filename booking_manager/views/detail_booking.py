from django.shortcuts import get_object_or_404, render
from booking_manager.models import Booking


def detail_booking(request, booking_id):
    template_name = 'detail_booking.html'

    context = {
        'details': get_object_or_404(Booking.objects
        .prefetch_related('products')
        .select_related('barber__user','client__user'),pk=booking_id)
    }

    return render(request, template_name=template_name, context=context)
