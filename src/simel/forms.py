from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            "idInstituto",
            "numeroControl",
            "coment",
            "idStatus",
            "idServicio",
            "idAcademia"
        ]      