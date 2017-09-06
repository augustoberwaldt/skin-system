from django.forms import ModelForm

from administrator.model import Disease


class FormDisease(ModelForm):
    class Meta:
        model = Disease.Disease
        fields = ['name', 'type', 'description']
