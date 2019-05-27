from django import forms

from .models import Carrera, Instituto, Materia, MateriaSolicitada, Solicitud


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

