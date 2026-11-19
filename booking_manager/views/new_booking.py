from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from booking_manager.forms.booking_form import BookingForm


@login_required
def new_booking(request):
    template_name = 'new_booking.html'
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            if hasattr(request.user, 'client'):

                    booking = form.save(commit=False)
                    booking.client = request.user.client
                    booking.save()

                    return HttpResponseRedirect(reverse('detail_booking', kwargs={'booking_id' : booking.id}))
        else:
            form.add_error(None, 'У вас нет профиля клиента. Вы не можете забронировать мастера.')
    else:
        form = BookingForm()


    return render(request, template_name=template_name, context={'form' : form })
