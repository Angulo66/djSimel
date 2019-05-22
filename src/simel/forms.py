from django import forms
from .models import Solicitud
from django.forms import ModelForm

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            "idInstituto",
            "numeroControl"
        ]      