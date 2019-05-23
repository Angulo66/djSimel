from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib import messages

from django.db.models.base import ObjectDoesNotExist

# Create your views here.
from django.http import HttpResponse
from .models import Instituto, Solicitud
from .forms import SolicitudForm

"""
def get_template(request):
    try:
        if request.is_authenticated:
            if request.groups.get(name="Jefatura"):
                print("jefatura")
            else:
                print("no existes")
    except Exception:
        print(Exception)
"""


def tablero(request):
    solicitudes = Solicitud.objects.all().count()
    solPend = Solicitud.objects.filter(idStatus=2).count()
    solRech = Solicitud.objects.filter(idStatus=4).count()
    solFin = Solicitud.objects.filter(idStatus=5).count()

    sisCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.id=1")
    ticsCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.id=2")
    bioCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.id=3")


    context = {
        "solicitudes": solicitudes,
        "pendientes": solPend,
        "rechazados": solRech,
        "finalizados": solFin,
        "contS": sisCont,
        "contT": ticsCont,
        "contB": bioCont
    }
    return render(request, 'base.html', context)


def solicitud(request):
    form = SolicitudForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Solicitud Enviada!")
    else:
        messages.error(request, "Error en enviar Solicitud!")    
    context = {
        "form": form
    }
    template = 'solicitud.html'
    return render(request, template, context)


def solicitud_detail(request, id=None):
    instance = get_object_or_404(Solicitud, id=id)
    context = {
        "title": instance.numControl,
        "instance": instance 
    }
    return render(request, '', context)


def solicitudes(request):
    solicitud = Solicitud.objects.raw("Select a.*,c.nombre as nomcarrera,i.instituto,ss.fechasolic,st.descstat from simel_solicitud ss inner join simel_alumno a on ss.numerocontrol_id=a.id inner join simel_carrera c on c.id=a.idcarrera_id inner join simel_status st on ss.idstatus_id=st.id inner join simel_instituto i on i.id=ss.idinstituto_id")
    context = {
        "solicitud": solicitud
    }
    template = 'solicitudes.html'
    return render(request, template, context)

