from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from datetime import date


class Usuario(models.Model):
    userName = models.CharField(("user"), max_length=50)
    password = models.CharField(("password"), max_length=50)
    tipoUsuario = models.IntegerField(("tipo de usuario"))
    is_active = models.BooleanField(("es usaurio activo"), default=True)
        
    def __str__(self):
        return self.userName

class Plan(models.Model):
    nombre = models.CharField(("plan"), max_length=50)
    semVal = models.IntegerField(("semestres de validacion"))
    coment = models.CharField(("comentarios"), max_length=320)


class Pais(models.Model):
    pais = models.CharField(("pais"), max_length=50)


class Estado(models.Model):
    estado = models.CharField(("estado"), max_length=50)
    idPais = models.ForeignKey(Pais, verbose_name=("id pais"), on_delete=models.CASCADE)        


class Municipio(models.Model):
    municipio = models.CharField(("municipio"), max_length=50)
    idEstado = models.ForeignKey(Estado, verbose_name=("id estado"), on_delete=models.CASCADE)


class Localidad(models.Model):
    localidad = models.CharField(("localidad"), max_length=50) 
    idMunicipio = models.ForeignKey(Municipio, verbose_name=("id municipio"), on_delete=models.CASCADE)


class Instituto(models.Model):
    instituto = models.CharField(("instituto"), max_length=50)
    idLocalidad = models.ForeignKey(Localidad, verbose_name=("id localidad"), on_delete=models.CASCADE)      


class Carrera(models.Model):
    nombre = models.CharField(("carrera"), max_length=50)
    especialidad = models.CharField(("especialidad"), max_length=50)
    idInstituto = models.ForeignKey(Instituto, verbose_name=("id instituto"), on_delete=models.CASCADE)


class Alumno(models.Model):
    numControl = models.IntegerField(("numero de control"))
    nombre = models.CharField(("nombre"), max_length=50)
    apellido = models.CharField(("apellido"), max_length=50)
    idCarrera = models.ForeignKey(Carrera, verbose_name=("carrera"), on_delete=models.CASCADE)
    idPlan = models.ForeignKey(Plan, verbose_name=("plan"), on_delete=models.CASCADE)
    promedio = models.DecimalField(("promedio"), max_digits=5, decimal_places=2)
    semestre = models.IntegerField(("semestre"))
    idUsuario = models.ForeignKey(Usuario, verbose_name=("nombre de usuario"), on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Aduedo(models.Model):
    numControl = models.ForeignKey(Alumno, verbose_name=(""), on_delete=models.CASCADE)
    creditosAcum = models.IntegerField(("creditos acumulados"))
    adeudo = models.BinaryField(("aduedo de libro"), default=0)
    cantMov = models.IntegerField(("cantidad de movilidades curados"))
    cursoVerano = models.BinaryField((""))
    coment = models.CharField(("commentario"), max_length=320)
    matRC = models.IntegerField(("materias cursadando en RC"))
    eligible = models.BooleanField(("Es eligible"), default=True)

    def is_eligable(self):
        if( self.matRC >= 2):
            self.coment += ('El alumno debe {}'.format(self.matRC))
            self.eligible = 
        if( self.creditosAcum < 150):
            self.coment += ' El alumno no cumple con los suficientes creditos' 
        if( self.cantMov >= 3):
            self.coment += ' El alumno ya paso el limite de movilidades' 
        if( self.adeudo == 1):
            self.coment += ' El alumno tiene adeudos'
        if( self.cursoVerano == 1):
            self.coment = 'Curso de verano'        
        return self.eligible 

class Materia(models.Model):
    materia = models.CharField(("materia"), max_length=50)
    creditos = models.IntegerField(("creditos"))
    idInstituto = models.ForeignKey(Instituto, verbose_name=("id instituto"), on_delete=models.CASCADE)
    idCarrera  = models.ForeignKey(Carrera, verbose_name=("id carrera"), on_delete=models.CASCADE)


class MateriasDelAlumno(models.Model):
    numControl = models.ForeignKey(Alumno, verbose_name=("numero de control"), on_delete=models.CASCADE)
    idMaterias = models.ForeignKey(Materia, verbose_name=("materia"), on_delete=models.CASCADE)
    idInstituto = models.ForeignKey(Instituto, verbose_name=("instituto"), on_delete=models.CASCADE)
    idCarrera = models.ForeignKey(Carrera, verbose_name=("carrera"), on_delete=models.CASCADE)
    calif = models.DecimalField(("calificacion"), max_digits=5, decimal_places=2)


class Jefatura(models.Model):
    nombre = models.CharField(("nombre"), max_length=50)
    apellido = models.CharField(("apellido"), max_length=50)
    idUsuario = models.ForeignKey(Usuario, verbose_name=(""), on_delete=models.CASCADE)


class Coordinador(models.Model):
    nombre = models.CharField(("nombre"), max_length=50)
    apellido = models.CharField(("apellido"), max_length=50)
    idCarrera = models.ForeignKey(Carrera, verbose_name=(""), on_delete=models.CASCADE)
    idJefatura = models.ForeignKey(Jefatura, verbose_name=("id jefatura"), on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, verbose_name=(""), on_delete=models.CASCADE)


class ServicioEscolar(models.Model):
    nombre = models.CharField(("nombre"), max_length=50)
    apellido = models.CharField(("apellido"), max_length=50)
    coment = models.CharField(("comentario"), max_length=320)
    idUsuario = models.ForeignKey(Usuario, verbose_name=(""), on_delete=models.CASCADE)


class Academia(models.Model):
    nombre = models.CharField(("nombre"), max_length=50)
    apellido = models.CharField(("apellido"), max_length=50)
    idUsuario = models.ForeignKey(Usuario, verbose_name=(""), on_delete=models.CASCADE)


class Status(models.Model):
    status = models.CharField(("status"), max_length=50)
    tipoStatus = models.IntegerField(("tipo de status") ,default=1)
    descStat = models.CharField(("descripcion"), max_length=50)


class Solicitud(models.Model):
    fechaSolic = models.DateField(("fecha de registro"), auto_now=True, auto_now_add=False)
    coment = models.CharField(("comentario"), max_length=320)
    idInstituto = models.ForeignKey(Instituto, verbose_name=("instituto"), on_delete=models.CASCADE)
    numeroControl = models.ForeignKey(Alumno, verbose_name=("numero de control"), on_delete=models.CASCADE)
    idStatus = models.ForeignKey(Status, verbose_name=("status"), on_delete=models.CASCADE)
    idServicio = models.ForeignKey(ServicioEscolar, verbose_name=("id servicio escolar"), on_delete=models.CASCADE)
    idAcademia = models.ForeignKey(Academia, verbose_name=("id academia"), on_delete=models.CASCADE)


class Movimiento(models.Model):
    idSolicitud = models.ForeignKey(Solicitud, verbose_name=("id solicitud"), on_delete=models.CASCADE)
    fecha = models.DateField(("fecha de movimiento"), auto_now=True, auto_now_add=False)
    usuario = models.ForeignKey(Usuario, verbose_name=(""), on_delete=models.CASCADE)
    idStatus = models.ForeignKey(Status, verbose_name=("id status"), on_delete=models.CASCADE)


class MateriaSolicitada(models.Model):
    idSolicitud = models.ForeignKey(Solicitud, verbose_name=("id solicitud"), on_delete=models.CASCADE)
    idMateria = models.ForeignKey(Materia, verbose_name=("id materia"), on_delete=models.CASCADE)
    idInstituto = models.ForeignKey(Instituto, verbose_name=("id instituto"), on_delete=models.CASCADE)
    idCarrera = models.ForeignKey(Carrera, verbose_name=(""), on_delete=models.CASCADE)
    calif = models.DecimalField(("calificacion"), max_digits=5, decimal_places=2)