from django.shortcuts import get_object_or_404, render
from booking_manager.models import Booking, Product


def product_shop(request, booking_id):
    template_name = 'product_shop.html'

    booking = get_object_or_404(Booking, id=booking_id)
    products =  Product.objects.filter(amount__gt=0)

    context = {
        'booking' : booking,
        'products' : products
    }

    return render(request, template_name=template_name, context=context)
