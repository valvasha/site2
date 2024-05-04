from django import forms

class Form(forms.Form):
    a = forms.FloatField(label="Ребро кубической ёмоксти = ")
    h = forms.FloatField(label="Высота целиндрической ёмоксти = ")
    r = forms.FloatField(label="Радиус основания целиндрической ёмоксти = ")
    m = forms.FloatField(label="Объём жидкости = ")