from django import forms
from django.forms.widgets import NumberInput, Textarea
from account.models import Barber


class CommentForm(forms.Form):
    barber = forms.ModelChoiceField(
        label='Выберите барбера',
        empty_label='-----Выбор мастера-----',
        queryset=Barber.objects.all()
    )

    text = forms.CharField(
        label='Введите комментарий',
        widget=Textarea(attrs={'style': 'resize: none'})
    )

    rating = forms.IntegerField(
        label='Оценка барбера',
        widget=NumberInput(
            attrs={'min' : 1, 'max' : 5})

    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['barber'].label_from_instance = lambda x: f'{x.user.first_name} {x.user.last_name}'

