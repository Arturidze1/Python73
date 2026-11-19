from django.shortcuts import render
from booking_manager.models import BookingService


def services(request):
    template_name = 'services.html'

    context = {
        'services': BookingService.objects.all()
    }
    return render(request, template_name=template_name, context=context)
