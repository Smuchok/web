from django import forms
from .models import *


class AddCategory(forms.Form):
    name = forms.CharField(max_length=32, label="Назва")
    have_limit = forms.BooleanField(label='Чи обмежена')


class AddGood(forms.Form):
    name = forms.CharField(max_length=32, label="Назва")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Виберіть категорію', label='Категорія')
    weight = forms.FloatField(label='Вага')
    price = forms.FloatField(label='Ціна')
