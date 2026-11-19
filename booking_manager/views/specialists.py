from django.db.models import Avg
from django.shortcuts import render
from account.models import Barber


def specialists(request):
    template_name = 'specialists.html'

    specialists = (Barber.objects
                   .select_related('user')
                   .annotate(avg_rating=Avg('received_comment__rating')))

    context={
        'specialists' : specialists
    }
    return render(request, template_name=template_name, context=context)
