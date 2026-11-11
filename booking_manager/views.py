from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Avg

from booking_manager.forms.booking_form import BookingForm
from booking_manager.forms.booking_service_form import BookingServiceForm
from booking_manager.forms.comment_form import CommentForm
from booking_manager.forms.product_booking_form import ProductBookingForm
from booking_manager.models import Booking, BookingService, Comment, Product, ProductBooking
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

    specialists = (Barber.objects
                   .select_related('user')
                   .annotate(avg_rating=Avg('received_comment__rating')))

    context={
        'specialists' : specialists
    }
    return render(request, template_name=template_name, context=context)

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


    return render(request, template_name=template_name, context={'form' : form })


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

def info_about_barber(request, barber_id):
    template_name = 'info_about_barber.html'

    barber = get_object_or_404(Barber.objects.select_related('user'), id=barber_id)

    comments = barber.received_comment.all()

    context = {
        'barber': barber,
        'comments': comments,
    }

    return render(request, template_name=template_name, context=context)


def product_shop(request, booking_id):
    template_name = 'product_shop.html'

    booking = get_object_or_404(Booking, id=booking_id)
    products =  Product.objects.filter(amount__gt=0)

    context = {
        'booking' : booking,
        'products' : products
    }

    return render(request, template_name=template_name, context=context)

def add_to_cart(request, booking_id, product_id):
    booking = get_object_or_404(Booking, id=booking_id)
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ProductBookingForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            product_booking, created = ProductBooking.objects.get_or_create(
                booking=booking,
                product=product,
                defaults={
                    'quantity': quantity,
                    'total_price': product.price * quantity,
                },
            )

            if not created:
                product_booking.quantity += quantity
                product_booking.total_price = product.price * product_booking.quantity
                product_booking.save(update_fields=['quantity', 'total_price'])

            product.amount -= quantity
            product.save(update_fields=['amount'])
            return redirect('product_shop', booking_id=booking.id)

    return redirect('product_shop', booking_id=booking.id)


def remove_from_booking(request, booking_id, product_booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id)
        product_booking = get_object_or_404(
            ProductBooking.objects.select_related('product'),
            id=product_booking_id,
            booking=booking,
        )

        product = product_booking.product
        product.amount += product_booking.quantity or 0
        product.save(update_fields=['amount'])
        product_booking.delete()

    return redirect('detail_booking', booking_id=booking_id)

