from django import forms
from django.forms import ModelForm
from .models import Author


class AuthorFrom(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')
        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'patronymic': 'Patronymic'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'})
        }
