from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from booking_manager.forms.booking_service_form import BookingServiceForm


def add_booking_service(request):
    template_name = 'add_booking_service.html'
    if request.method == "POST":
        form = BookingServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = BookingServiceForm()

    return render(request, template_name=template_name, context={'form' : form})
