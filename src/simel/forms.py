from django import forms
from .models import Solicitud

class LoginForm(forms.Form):
    username = forms.CharField(max_length=320)
    password = forms.CharField(required=True)