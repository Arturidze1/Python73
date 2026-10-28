from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from booking_manager.models import Booking, BookingService
from account.models import Barber

def index(request):
    return HttpResponse("Hello, world. You're at the booking_manager index.")

def home(request):
    return render(request, 'home.html')

def services(request):
    template_name = 'services.html'

    context = {
        'services': BookingService.objects.all()
    }
    return render(request, template_name=template_name, context=context)

def specialists(request):
    template_name = 'specialists.html'

    context = {
        'specialists' : Barber.objects
            .select_related('user')
            .prefetch_related('received_comment')
    }
    return render(request, template_name=template_name, context=context)

def bookings(request):

    template_name = 'bookings.html'
    context = {
        'bookings': Booking.objects
        .select_related(
            'client__user',
            'barber__user'
        )
    }
    return render(request, template_name=template_name, context=context)

def detail_booking(request, booking_id):
    template_name = 'detail_booking.html'

    context = {
        'details': get_object_or_404(Booking.objects
        .prefetch_related('products')
        .select_related('barber__user','client__user'),pk=booking_id)
    }

    return render(request, template_name=template_name, context=context)

def new_booking(request):
    return render(request, 'new_booking.html')
