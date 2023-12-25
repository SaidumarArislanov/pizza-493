from django import forms
from .models import RegistrationModel


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        fields = ['name', 'email', 'phone', 'date', 'time', 'message']
