from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from booking_manager.models import Booking, Product


@require_POST
def cancel_booking(request, booking_id):
    with transaction.atomic():
        booking = get_object_or_404(
            Booking.objects.select_for_update(),
            id=booking_id,
        )

        if booking.is_active:
            items = booking.products_to_book.order_by('product_id')
            for item in items:
                product = Product.objects.select_for_update().get(id=item.product_id)
                product.amount += item.quantity or 0
                product.save(update_fields=['amount'])

            booking.is_active = False
            booking.save(update_fields=['is_active'])

    return redirect('detail_booking', booking_id=booking_id)
