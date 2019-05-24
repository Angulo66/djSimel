from django import forms
from .models import MateriaSolicitada, Solicitud, Materia, Instituto, Carrera


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            "coment",
            "idInstituto",
            "numeroControl",
            "idStatus",
            "idServicio",
            "idAcademia"
        ]
        widgets = {'idStatus': forms.HiddenInput()}


class MateriaSolicitadaForm(forms.ModelForm):
    class Meta:
        model = MateriaSolicitada
        fields = [
            "idSolicitud",
            "idMateria",
            "idInstituto",
            "idCarrera",
            "calif"
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['idMateria'].queryset = Materia.objects.none()