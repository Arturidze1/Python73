from django.shortcuts import get_object_or_404, render
from account.models import Barber


def info_about_barber(request, barber_id):
    template_name = 'info_about_barber.html'

    barber = get_object_or_404(Barber.objects.select_related('user'), id=barber_id)

    comments = barber.received_comment.all()

    context = {
        'barber': barber,
        'comments': comments,
    }

    return render(request, template_name=template_name, context=context)
