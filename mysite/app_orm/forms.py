from django import forms
from django.forms import ModelForm
from .models import AbcModel

# class Form(forms.Form):
#     a = forms.FloatField(label="Ребро кубической ёмоксти = ")
#     h = forms.FloatField(label="Высота целиндрической ёмоксти = ")
#     r = forms.FloatField(label="Радиус основания целиндрической ёмоксти = ")
#     m = forms.FloatField(label="Объём жидкости = ")

class AbcModelForm(ModelForm):
    class Meta:
        model = AbcModel
        fields = '__all__'
        exclude = ('result', 'tusk', 'datetime',)