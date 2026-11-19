from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from booking_manager.models import Booking, Product, ProductBooking


@require_POST
def remove_from_booking(request, booking_id, product_booking_id):
    with transaction.atomic():
        booking = get_object_or_404(
            Booking.objects.select_for_update(),
            id=booking_id,
        )
        product_booking = get_object_or_404(
            ProductBooking.objects.select_for_update(),
            id=product_booking_id,
            booking=booking,
        )

        if booking.is_active:
            product = Product.objects.select_for_update().get(pk=product_booking.product_id)
            product.amount += product_booking.quantity or 0
            product.save(update_fields=['amount'])

        product_booking.delete()

    return redirect('detail_booking', booking_id=booking_id)
