from django.shortcuts import get_object_or_404, redirect
from booking_manager.forms.product_booking_form import ProductBookingForm
from booking_manager.models import Booking, Product, ProductBooking


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

            return redirect('product_shop', booking_id=booking.id)

    return redirect('product_shop', booking_id=booking.id)
