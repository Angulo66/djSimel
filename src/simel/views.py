from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, User
from django.db.models.base import ObjectDoesNotExist
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render, reverse)
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import MateriaSolicitadaForm, SolicitudForm
from .models import (Alumno, Instituto, Materia, MateriaSolicitada, Solicitud,
                     Status, Academia, ServicioEscolar)

# COUNT carreras por departamento

sisCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Sistemas\'")
ticsCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.id=\'Ing. TICs\'")
bioCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Bioquimica\'")
eleCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Electronica\'")
elcCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Electrica\'")
indCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Industrial\'")
mecCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Mecanica\'")
mechCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Mecatronica\'")
eneCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Energias Renovables\'")
ambCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Ambiental\'")
empCont = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Gestion Empreserial\'")

# COUNT Solicitudes & Status

solicitudesC = Solicitud.objects.all().count()
pendientes = Solicitud.objects.filter(idStatus=2).count()
aceptados = Solicitud.objects.filter(idStatus=3).count()
rechazados = Solicitud.objects.filter(idStatus=4).count()
finalizados = Solicitud.objects.filter(idStatus=5).count()

def tablero(request):
    count_status_coord = Solicitud.objects.raw("SELECT 1 as id, COUNT(*) as total, COUNT( case when st.status='Finalizado' then st.status end) as finalizado, COUNT( case when st.status='Acpetado' then st.status end) as aceptado, COUNT( case when st.status='Enviado' then st.status end) as enviado, COUNT( case when st.status='Rechazado' then st.status end) as rechazado, COUNT( case when st.status='Pendiente' then st.status end) as pendiente FROM auth_user au INNER JOIN simel_coordinador sc ON au.id=sc.idUsuario_id INNER JOIN simel_carrera ss ON ss.idCoordinador_id=sc.id INNER JOIN simel_alumno sa ON sa.idCarrera_id=ss.id INNER JOIN simel_solicitud sp ON sp.numeroControl_id=sa.id INNER JOIN simel_instituto si ON si.id=sp.idInstituto_id INNER JOIN simel_status st ON st.id=sp.idStatus_id WHERE au.username='{}'".format(request.user.username))
    
    is_escolar = Solicitud.objects.raw("select 1 as id, count(*) as existe from simel_servicioescolar e inner join auth_user au on au.id=idusuario_id where au.username='{}'".format(request.user.username))
    is_academia = Solicitud.objects.raw("select 1 as id, count(*) as existe from simel_academia e inner join auth_user au on au.id=idusuario_id where au.username='{}'".format(request.user.username))
    
    for a in is_escolar:
        esc = a.existe is not 0 # True if 1

    for a in is_academia:
        acc = a.existe is not 0 # False is 0   
    
    context = {
        "solicitudes": solicitudesC, "contCoord": count_status_coord,
        "pendientes": pendientes, "escolar": esc,
        "rechazados": rechazados,  "academia": acc,
        "finalizados": finalizados,
        "contS": sisCont, "contEl": elcCont, "contEr": eneCont,
        "contT": ticsCont, "contI": indCont, "contA": ambCont,
        "contB": bioCont, "contM": mecCont, "contEm": empCont,
        "contE": eleCont, "contMc": mechCont
    }
    return render(request, 'base.html', context)


def servicio(request):
    template = 'servicio.html'
    context = {
    }
    return render(request, template, context)


def solicitud(request):
    form = SolicitudForm
    datos_personales = Solicitud.objects.raw("SELECT 1 as id, a.numcontrol as numcontrol ,a.nombre ||' '||a.apellido as nombre,sc.nombre as carrera, sc.especialidad as esp ,a.semestre FROM simel_alumno a inner join auth_user au on a.idusuario_id=au.id  inner join  simel_carrera sc on sc.id=a.idcarrera_id WHERE au.username={}".format(request.user.username))
    template = 'simel/solicitud_form.html'
    context = {
        "titulo": "Datos Personales",
        "datos": datos_personales,
        "form": form
    }
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


class SolicitudListView(ListView):
    model = Solicitud
    context_object_name = 'solicitud_changelist'


class SolicitudCreateView(LoginRequiredMixin , CreateView):
    model = Solicitud
    fields = '__all__'

    def get_initial(self):
        return {
            'numeroControl': Alumno.objects.get(numControl=self.request.user.username),
            'idStatus': Status.objects.get(status="Enviado"),
            'idAcademia': Academia.objects.get(nombre="academia"),
            'idServicio': ServicioEscolar.objects.get(nombre="escolar")
        }

    def get_success_url(self):
        return reverse('solicitud_changelist')        


class SolicitudUpdateView(UpdateView):
    model = Solicitud
    form = SolicitudForm
    fields = ("coment", 
            "idInstituto",
            "numeroControl",
            "idStatus",
            "idServicio",
            "idAcademia")
    success_url = reverse_lazy('solicitud_changelist')


# Materias Solicitadas Mixins ===============================

class MateriaSolicitadaListView(ListView):
    model = MateriaSolicitada
    context_object_name = 'materia'


class MateriaSolicitdadCreateView(CreateView):
    model = MateriaSolicitada
    form = MateriaSolicitadaForm
    fields = ('idSolicitud','idMateria','idInstituto','idCarrera','calif')
    success_url = reverse_lazy('materia_changelist')


class MateriaSolicitdadUpdateView(UpdateView):
    model = MateriaSolicitada
    form = MateriaSolicitadaForm
    fields = ('idSolicitud','idMateria','idInstituto','idCarrera','calif')
    success_url = reverse_lazy('materia_changelist')

def load_materias(request):
    materia_solicitada_id = request.GET.get('idMateria')
    materias = Materia.objects.filter(materia_solicitada_id=materia_solicitada_id).orderby('idSolicitud')
    return render(request, 'simel/materia_dropdown_list_options.html', {'materias': materias})
