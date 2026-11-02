from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from booking_manager.forms.booking_form import BookingForm
from booking_manager.forms.booking_service_form import BookingServiceForm
from booking_manager.forms.comment_form import CommentForm
from booking_manager.models import Booking, BookingService, Comment
from account.models import Barber, Client


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

                return HttpResponseRedirect(reverse('home'))
        else:
            form.add_error(None, 'У вас нет профиля клиента. Вы не можете забронировать мастера.')
    else:
        form = BookingForm()

    return render(request, template_name=template_name, context={'form' : form})


@login_required
def add_comments(request):
    template_name = 'add_comments.html'
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if hasattr(request.user, 'client'):

                barber = form.cleaned_data['barber']
                text = form.cleaned_data['text']
                rating = form.cleaned_data['rating']

                Comment.objects.create(
                    barber=barber,
                    text=text,
                    rating=rating,
                    client= request.user.client,
                    is_published=False
                )

            return HttpResponseRedirect(reverse('specialists'))
        else:
            form.add_error(None, 'У вас нет профиля клиента. Вы не можете оставить комментарий.')
    else:
        form = CommentForm()

    return render(request, template_name=template_name, context={'form' : form})


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
