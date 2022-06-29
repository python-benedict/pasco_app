from django import forms
from .models import Register

class RegistrationForms(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'