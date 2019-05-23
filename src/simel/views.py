from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
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

    sisCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Sistemas\'")
    ticsCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.id=2")
    bioCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Bioquimica\'")
    eleCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Electronica\'")
    elcCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Electrica\'")
    indCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Industrial\'")
    mecCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Mecanica\'")
    mechCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Mecatronica\'")
    eneCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Energias Renovables\'")
    ambCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Ambiental\'")
    empCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Gestion Empreserial\'")

    contCoord = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as total, COUNT( case when st.status='Finalizado' then st.status end) as finalizado, COUNT( case when st.status='Acpetado' then st.status end) as aceptado, COUNT( case when st.status='Enviado' then st.status end) as enviado, COUNT( case when st.status='Rechazado' then st.status end) as rechazado, COUNT( case when st.status='Pendiente' then st.status end) as pendiente FROM auth_user au INNER JOIN simel_coordinador sc ON au.id=sc.idUsuario_id INNER JOIN simel_carrera ss ON ss.idCoordinador_id=sc.id INNER JOIN simel_alumno sa ON sa.idCarrera_id=ss.id INNER JOIN simel_solicitud sp ON sp.numeroControl_id=sa.id INNER JOIN simel_instituto si ON si.id=sp.idInstituto_id INNER JOIN simel_status st ON st.id=sp.idStatus_id WHERE au.username='{}'".format(request.user.username))
    
    is_escolar = Solicitud.objects.raw("select 1 as id, count(*) as existe from simel_servicioescolar e inner join auth_user au on au.id=idusuario_id where au.username='{}'".format(request.user.username))
    is_academia = Solicitud.objects.raw("select 1 as id, count(*) as existe from simel_academia e inner join auth_user au on au.id=idusuario_id where au.username='{}'".format(request.user.username))
    

    for a in is_escolar:
        esc = a.existe is not 0 # True if 1

    for a in is_academia:
        acc = a.existe is not 0 # False is 0   
    
    context = {
        "solicitudes": solicitudes, "contCoord": contCoord,
        "pendientes": solPend, "escolar": esc,
        "rechazados": solRech,  "academia": acc,
        "finalizados": solFin,
        "contS": sisCont, "contEl": elcCont, "contEr": eneCont,
        "contT": ticsCont, "contI": indCont, "contA": ambCont,
        "contB": bioCont, "contM": mecCont, "contEm": empCont,
        "contE": eleCont, "contMc": mechCont
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
    solcoord = Solicitud.objects.raw("SELECT 1 as id, sa.numControl, sc.nombre, ss.nombre as carrera, sa.nombre as alumno, sp.fechaSolic as fecha, si.instituto, st.status as status FROM auth_user au INNER JOIN simel_coordinador sc ON au.id=sc.idUsuario_id INNER JOIN simel_carrera ss ON ss.idCoordinador_id=sc.id INNER JOIN simel_alumno sa ON sa.idCarrera_id=ss.id INNER JOIN simel_solicitud sp ON sp.numeroControl_id=sa.id INNER JOIN simel_instituto si ON si.id=sp.idInstituto_id INNER JOIN simel_status st ON st.id=sp.idStatus_id WHERE au.username='{}'".format(request.user.username))
    context = {
        "solicitud": solicitud,
        "coordS": solcoord
    }
    template = 'solicitudes.html'
    return render(request, template, context)

