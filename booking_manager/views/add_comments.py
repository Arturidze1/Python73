from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from booking_manager.forms.comment_form import CommentForm
from booking_manager.models import Comment


@login_required
def add_comments(request):
    template_name = 'add_comments.html'
    if request.method == "POST":
        form = CommentForm(request.POST)
        if hasattr(request.user, 'client'):
            if form.is_valid():

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
