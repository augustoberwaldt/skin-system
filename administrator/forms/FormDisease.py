
from django import  forms

class FormDisease(forms.Form):
    name = forms.CharField()
    type = forms.CharField()
    description = forms.CharField()