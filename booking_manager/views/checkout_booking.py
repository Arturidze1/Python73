from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from booking_manager.models import Booking, Product


@require_POST
def checkout_booking(request, booking_id):
    try:
        with transaction.atomic():
            booking = get_object_or_404(
                Booking.objects.select_for_update(),
                id=booking_id,
            )

            if not booking.is_active:
                items = booking.products_to_book.order_by('product_id')
                for item in items:
                    product = Product.objects.select_for_update().get(id=item.product_id)
                    quantity = item.quantity
                    if quantity is None or product.amount < quantity:
                        raise ValueError('Товаров недостаточно на складе')

                    product.amount -= quantity
                    product.save(update_fields=['amount'])

                booking.is_active = True
                booking.save(update_fields=['is_active'])

    except ValueError as error:
        messages.error(request, str(error))

    return redirect('detail_booking', booking_id=booking_id)
