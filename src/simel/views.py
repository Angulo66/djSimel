from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import (get_object_or_404, get_list_or_404 , render, reverse)
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.models import User
from .forms import SolicitudForm, MateriaSolicitadaForm
from .models import (Alumno, Materia, MateriaSolicitada, Solicitud, Aduedo,
                     Status, Academia, ServicioEscolar, Instituto, Movimiento)


obj = Solicitud.objects


# COUNT carreras departamento

sisCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa "+
"ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Sistemas\'")
ticsCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa "+
"ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. TICs\'")
bioCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa "+
"ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Bioquimica\'")
eleCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON "+
"ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Electronica\'")
elcCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON "+
"ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Electrica\'")
indCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON "+
"ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Industrial\'")
mecCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON "+
"ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Mecanica\'")
mechCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON "+
"ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Mecatronica\'")
eneCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Energias Renovables\'")
ambCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Ambiental\'")
empCont = obj.raw("SELECT 1 as id, COUNT(*) as contador  FROM simel_solicitud ss INNER JOIN simel_alumno sa ON ss.numerocontrol_id=sa.id INNER JOIN simel_carrera sc ON sc.id=sa.idcarrera_id WHERE sc.nombre=\'Ing. Gestion Empreserial\'")
soldate = obj.raw("SELECT 1 as id, count(case WHEN strftime('%m',fechaSolic)='01' then 1 end) as enero,count(case WHEN strftime('%m',fechaSolic)='02' then 1 end) as febrero,count(case WHEN strftime('%m',fechaSolic)='03' then 1 end) as marzo,count(case WHEN strftime('%m',fechaSolic)='04' then 1 end) as abril,count(case WHEN strftime('%m',fechaSolic)='05' then 1 end) as mayo from simel_solicitud")
datecount =[]
contadores =[sisCont, elcCont, eneCont,ticsCont,indCont,ambCont,bioCont, mecCont, empCont,eleCont, mechCont]

porcent=[]

for a in soldate:
    datecount=[a.enero,a.febrero,a.marzo,a.abril,a.mayo]

total=obj.all().count()

for a in contadores:
    for b in a:
        t=0
        if(total!=0):
            t=(b.contador*100)/total
        porcent.append(t)


def capturarView(request):
    template = 'capturar_list.html'
    solicitud = obj.raw("SELECT 1 as id,sp.id as idsoli, sa.numControl, sc.nombre, ss.nombre as carrera, sa.nombre as "+
    "alumno, sp.fechaSolic as fecha, si.instituto, st.status as status FROM auth_user au INNER JOIN simel_coordinador sc "+
    "ON au.id=sc.idUsuario_id INNER JOIN simel_carrera ss ON ss.idCoordinador_id=sc.id INNER JOIN simel_alumno sa "+
    "ON sa.idCarrera_id=ss.id INNER JOIN simel_solicitud sp ON sp.numeroControl_id=sa.id INNER JOIN simel_instituto si "+
    "ON si.id=sp.idInstituto_id INNER JOIN simel_status st ON st.id=sp.idStatus_id where sp.idstatus_id=5")
    context = {
        "solicitud": solicitud
    }
    return render(request, template, context)


def capturaDetail(request, id=None):
    template = 'capturar_form.html'
    instance = get_object_or_404(Solicitud, id=id)
    adeudo = get_object_or_404(Aduedo, numControl=instance.numeroControl)
    materias = MateriaSolicitada.objects.filter(idSolicitud=instance.id)
    movimientos = Movimiento.objects.filter(idSolicitud=instance.id)

    is_escolar = obj.raw("select 1 as id, count(*) as existe from simel_servicioescolar e "+
    "inner join auth_user au on au.id=idusuario_id where au.username='{}'".format(request.user.username))
    is_academia = obj.raw("select 1 as id, count(*) as existe from simel_academia e "+
    "inner join auth_user au on au.id=idusuario_id where au.username='{}'".format(request.user.username))
    
    for a in is_escolar:
        auth_escolar = a.existe is not 0 # True if 1

    for a in is_academia:
        auth_academia = a.existe is not 0 # False is 0
   
    for m in materias:
        print(m.idMateria)

    context = {
        "title": instance.coment,
        "instance": instance,
        "adeudo": adeudo,
        "materias": materias,
        "movimientos": movimientos,
        "academia": auth_academia,
        }
    print("Captura detail")
    return render(request, template, context)


def create_solicitud(request):
    if request.method =='POST':
        instituto = request.POST['instituto']
        numecontrol = request.POST['numero']
        materia= request.POST.getlist('materia[]')
        nid=0
        nins=solcoord = Solicitud.objects.raw("SELECT si.id from simel_instituto si WHERE si.instituto='{}'".format(instituto))
        for i in nins:
            nid=i.id
        print(materia)
        ins = Instituto.objects.get(pk =nid)
        al = Alumno.objects.get(pk=numecontrol)
        st = Status.objects.get(pk= 1)
        serv = ServicioEscolar.objects.get(pk= 1)
        aca = Academia.objects.get(pk= 1)
        a=Solicitud(
            coment =request.POST['comntario'] ,
            idInstituto = ins,
            numeroControl = al,
            idStatus =  st,
            idServicio = serv,
            idAcademia =aca
        )
        a.save()
        query = Solicitud.objects.raw("SELECT id,materia from simel_materia")
        for a in materia:
            for i in query:
                if(i.materia==a):
                    detalle=MateriaSolicitada(
                          idSolicitud = Solicitud.objects.all().last(),
                          idMateria = Materia.objects.get(pk=i.id) ,
                          idInstituto =ins, 
                          idCarrera = Materia.objects.get(pk=i.id).idCarrera,
                          calif =0.00,
                    )
                    detalle.save()
        m = Movimiento(
               idSolicitud = Solicitud.objects.all().last(),
               usuario = al.idUsuario,
               idStatus = st
        )
        m.save()
    return HttpResponse('')


def convalidarView(request):
    template = 'convalidar.html'
    solcoord = obj.raw("SELECT 1 as id,sp.id as idsoli, sa.numControl, sc.nombre, ss.nombre as carrera, sa.nombre as alumno, sp.fechaSolic as fecha, si.instituto, st.status as status FROM auth_user au INNER JOIN simel_coordinador sc ON au.id=sc.idUsuario_id INNER JOIN simel_carrera ss ON ss.idCoordinador_id=sc.id INNER JOIN simel_alumno sa ON sa.idCarrera_id=ss.id INNER JOIN simel_solicitud sp ON sp.numeroControl_id=sa.id INNER JOIN simel_instituto si ON si.id=sp.idInstituto_id INNER JOIN simel_status st ON st.id=sp.idStatus_id WHERE au.username='{}'".format(request.user.username))
    solicitud = obj.raw("SELECT 1 as id,sp.id as idsoli, sa.numControl, sc.nombre, ss.nombre as carrera, sa.nombre as alumno, sp.fechaSolic as fecha, si.instituto, st.status as status FROM auth_user au INNER JOIN simel_coordinador sc ON au.id=sc.idUsuario_id INNER JOIN simel_carrera ss ON ss.idCoordinador_id=sc.id INNER JOIN simel_alumno sa ON sa.idCarrera_id=ss.id INNER JOIN simel_solicitud sp ON sp.numeroControl_id=sa.id INNER JOIN simel_instituto si ON si.id=sp.idInstituto_id INNER JOIN simel_status st ON st.id=sp.idStatus_id")
    
    context = {
        "solicitud": solicitud,
        "coordS": solcoord
    }
    template = 'solicitudes.html'
    return render(request, template, context)


def convalidarMateria(request, id=None):
    instance = get_object_or_404(Solicitud, id=id)
    materias = MateriaSolicitada.objects.filter(idSolicitud=instance.id)
    template = 'convalidar.html'
    context = {
        "title": instance.numeroControl,
        "instance": instance,
        "materias": materias,
    }
    print("Materias del alumno")
    return render(request, template, context)


def solicitud_detail(request, id=None):
    instance = get_object_or_404(Solicitud, id=id)
    context = {
        "title": instance.numControl,
        "instance": instance
    }
    return render(request, '', context)


def solicitud(request):
    datos_personales = Solicitud.objects.raw("SELECT a.id as id, a.numcontrol as numcontrol ,a.nombre ||' '||a.apellido as nombre,sc.nombre as carrera, sc.especialidad as esp ,a.semestre FROM simel_alumno a inner join auth_user au on a.idusuario_id=au.id  inner join  simel_carrera sc on sc.id=a.idcarrera_id WHERE au.username={}".format(request.user.username))
    paises = Solicitud.objects.raw("SELECT 1 as id, sp.pais From simel_pais sp")
    template = 'solicitud.html'
    seme = ["","Primer","Segundo","Tercer","Cuarto","Quinto","Sexto","Septimo","Octavo","Noveno","Decimo","Onceavo","Doceavo"]
    x=0
    carrera=''
    id =0
    for i in datos_personales:
        x=i.semestre
        carrera=i.carrera
        id =i.id
    lugares = Solicitud.objects.raw("SELECT 1 as id, e.estado,sp.pais,m.municipio,c.localidad,i.instituto,mm.materia FROM simel_estado e inner join simel_pais sp  on sp.id=e.idpais_id inner join simel_municipio m on m.idestado_id=e.id inner join simel_localidad c on c.idmunicipio_id=m.id inner join simel_instituto i on c.id=i.idlocalidad_id left join simel_materia mm on mm.idinstituto_id=i.id inner join simel_carrera sc on sc.id=mm.idcarrera_id Where sc.nombre='{}'".format(carrera))
    context = {
        "titulo": "Datos Personales",
        "datos": datos_personales,
        "id": id,
        "paises": paises,
        "lugares": lugares,
        "sem":seme[x]
    }
    return render(request, template, context)


def solicitudDetail(request, id=None):
    template = 'solicitud_detail.html'
    instance = get_object_or_404(Solicitud, id=id)
    adeudo = get_object_or_404(Aduedo, numControl=instance.numeroControl)
    materias = MateriaSolicitada.objects.filter(idSolicitud=instance.id)
    movimientos = Movimiento.objects.filter(idSolicitud=instance.id)
    
    for m in materias:
        print("hola")
    eligible = False
    if adeudo.eligible:
        eligible = True

    context = {
        "title": instance.coment,
        "instance": instance,
        "adeudo": adeudo,
        "eligible": eligible,
        "materias": materias,
        "movimientos": movimientos,
        }
    print("Solicitud detail view")
    return render(request, template, context)


def solicitudEnviado(request):
    template = 'sent_status.html'
    context = {
    }
    return render(request, template, context)


def solicitudes(request):
    solcoord = obj.raw("SELECT 1 as id,sp.id as idsoli, sa.numControl, sc.nombre, ss.nombre as carrera, sa.nombre as alumno, sp.fechaSolic as fecha, si.instituto, st.status as status FROM auth_user au INNER JOIN simel_coordinador sc ON au.id=sc.idUsuario_id INNER JOIN simel_carrera ss ON ss.idCoordinador_id=sc.id INNER JOIN simel_alumno sa ON sa.idCarrera_id=ss.id INNER JOIN simel_solicitud sp ON sp.numeroControl_id=sa.id INNER JOIN simel_instituto si ON si.id=sp.idInstituto_id INNER JOIN simel_status st ON st.id=sp.idStatus_id WHERE au.username='{}'".format(request.user.username))
    solicitud = obj.raw("SELECT 1 as id,sp.id as idsoli, sa.numControl, sc.nombre, ss.nombre as carrera, sa.nombre as alumno, sp.fechaSolic as fecha, si.instituto, st.status as status FROM auth_user au INNER JOIN simel_coordinador sc ON au.id=sc.idUsuario_id INNER JOIN simel_carrera ss ON ss.idCoordinador_id=sc.id INNER JOIN simel_alumno sa ON sa.idCarrera_id=ss.id INNER JOIN simel_solicitud sp ON sp.numeroControl_id=sa.id INNER JOIN simel_instituto si ON si.id=sp.idInstituto_id INNER JOIN simel_status st ON st.id=sp.idStatus_id")
    
    context = {
        "solicitud": solicitud,
        "coordS": solcoord
    }
    template = 'solicitudes.html'
    return render(request, template, context)


def solicitudStatus(request):
    template = 'solicitud_status.html'
    context = {
    }
    return render(request, template, context)


def modificarSolicitud(request):
    if request.method =='POST':
        soli=Solicitud.objects.get(pk=request.POST['solicitud'])
        soli.idStatus=Status.objects.get(pk=request.POST['status'])
        soli.save()
        m = Movimiento(
               idSolicitud = Solicitud.objects.all().last(),
               usuario = User.objects.get(pk=request.POST['usuario']),
               idStatus = Status.objects.get(pk=request.POST['status'])
        )
        m.save()
    return HttpResponse('')


def tablero(request): 
    count_status_coord = obj.raw("SELECT 1 as id, COUNT(*) as total, "+
    "COUNT( case when st.status='Finalizado' then st.status end) as finalizado, "+
    "COUNT( case when st.status='Aceptado' then st.status end) as aceptado, "+
    "COUNT( case when st.status='Enviado' then st.status end) as enviado, "+
    "COUNT( case when st.status='Rechazado' then st.status end) as rechazado, "+
    "COUNT( case when st.status='Pendiente' then st.status end) as pendiente FROM auth_user au "+
    "INNER JOIN simel_coordinador sc ON au.id=sc.idUsuario_id INNER JOIN simel_carrera ss ON ss.idCoordinador_id=sc.id "+
    "INNER JOIN simel_alumno sa ON sa.idCarrera_id=ss.id INNER JOIN simel_solicitud sp ON sp.numeroControl_id=sa.id "+
    "INNER JOIN simel_instituto si ON si.id=sp.idInstituto_id INNER JOIN simel_status st ON st.id=sp.idStatus_id "+
    "WHERE au.username='{}'".format(request.user.username))
    
    is_escolar = obj.raw("select 1 as id, count(*) as existe from simel_servicioescolar e "+
    "inner join auth_user au on au.id=idusuario_id where au.username='{}'".format(request.user.username))
    is_academia = obj.raw("select 1 as id, count(*) as existe from simel_academia e "+
    "inner join auth_user au on au.id=idusuario_id where au.username='{}'".format(request.user.username))
    
    for a in is_escolar:
        auth_escolar = a.existe is not 0 # True if 1

    for a in is_academia:
        auth_academia = a.existe is not 0 # False is 0

    p = obj.filter(idStatus=2).count()
    f = obj.filter(idStatus=5).count()
    r = obj.filter(idStatus=4).count()
 
 

    context = {
        "solicitudes": obj.all().count(),
        "rechazados": r,
        "finalizados": f,
        "aceptados": obj.filter(idStatus=3).count(),
        "pendientes": p,
        "contCoord": count_status_coord,

        "escolar": auth_escolar,
        "academia": auth_academia,

        "last": obj.raw("select * from simel_solicitud order by id desc limit 3"),
        "alert_count": obj.all().count(),

        'array': [p, f, r],
        'date':datecount,
        "contS": sisCont, "contEl": elcCont, "contEr": eneCont,
        "contT": ticsCont, "contI": indCont, "contA": ambCont,
        "contB": bioCont, "contM": mecCont, "contEm": empCont,
        "contE": eleCont, "contMc": mechCont,
        'psistemas':porcent[0],
        'pelectronic':porcent[1],
        'pener':porcent[2],
        'ptics':porcent[3],
        'pind':porcent[4],
        'pamb':porcent[5],
        'pbio':porcent[6], 
        'pmec':porcent[7], 
        'pemp':porcent[8],
        'pelc':porcent[9], 
        'pmecan':porcent[10]
    }
    return render(request, 'base.html', context)


