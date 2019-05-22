from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from datetime import date


class Plan(models.Model):
    nombre = models.CharField(("plan"), max_length=50)
    semVal = models.IntegerField(("semestres de validacion"))
    coment = models.CharField(("comentarios"), max_length=320)

    def __str__(self):
        return self.nombre


class Pais(models.Model):
    pais = models.CharField(("pais"), max_length=50)

    def __str__(self):
        return self.pais


class Estado(models.Model):
    estado = models.CharField(("estado"), max_length=50)
    idPais = models.ForeignKey(Pais, verbose_name=("id pais"), on_delete=models.CASCADE)   

    def __str__(self):
        return self.estado     


class Municipio(models.Model):
    municipio = models.CharField(("municipio"), max_length=50)
    idEstado = models.ForeignKey(Estado, verbose_name=("id estado"), on_delete=models.CASCADE)

    def __str__(self):
        return self.municipio


class Localidad(models.Model):
    localidad = models.CharField(("localidad"), max_length=50) 
    idMunicipio = models.ForeignKey(Municipio, verbose_name=("id municipio"), on_delete=models.CASCADE)

    def __str__(self):
        return self.localidad


class Instituto(models.Model):
    instituto = models.CharField(("instituto"), max_length=50)
    idLocalidad = models.ForeignKey(Localidad, verbose_name=("id localidad"), on_delete=models.CASCADE)

    def __str__(self):
        return self.instituto      







"""
    def is_eligable(self):
        if( self.matRC >= 2):
            self.coment += ('El alumno debe {}'.format(self.matRC))
            self.eligible = False
        if( self.creditosAcum < 150):
            self.coment += ' El alumno no cumple con los suficientes creditos'
            self.eligible = False 
        if( self.cantMov >= 3):
            self.coment += ' El alumno ya paso el limite de movilidades'
            self.eligible = False 
        if( self.adeudo == 1):
            self.coment += ' El alumno tiene adeudos'
            self.eligible = False
        if( self.cursoVerano == 1):
            self.coment = 'Curso de verano'
            self.eligible = 'True'        
        return self.eligible 

    def __str__(self):
        if(self.eligible == True):
            return "Es eligible para Movilidad"
        else:
            return "No es eligible"   
"""


class Jefatura(models.Model):
    nombre = models.CharField(("nombre"), max_length=50)
    apellido = models.CharField(("apellido"), max_length=50)
    idUsuario = models.ForeignKey(User, verbose_name=("id usuario"), on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + '' + self.apellido


class Coordinador(models.Model):
    nombre = models.CharField(("nombre"), max_length=50)
    apellido = models.CharField(("apellido"), max_length=50)
    idJefatura = models.ForeignKey(Jefatura, verbose_name=("id jefatura"), on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(User, verbose_name=("id usuario"), on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido 


class Carrera(models.Model):
    nombre = models.CharField(("carrera"), max_length=50)
    especialidad = models.CharField(("especialidad"), max_length=50, default='')
    idCoordinador = models.ForeignKey(Coordinador, verbose_name="id coordinador", on_delete=models.CASCADE)
    idInstituto = models.ForeignKey(Instituto, verbose_name=("id instituto"), on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def get_esp(self):
        esp = ''
        if(self.especialidad != ''):
            esp = self.especialidad

        return esp


class Alumno(models.Model):
    numControl = models.IntegerField(("numero de control"))
    nombre = models.CharField(("nombre"), max_length=50)
    apellido = models.CharField(("apellido"), max_length=50)
    idCarrera = models.ForeignKey(Carrera, verbose_name=("carrera"), on_delete=models.CASCADE)
    idPlan = models.ForeignKey(Plan, verbose_name=("plan"), on_delete=models.CASCADE)
    promedio = models.DecimalField(("promedio"), max_digits=5, decimal_places=2)
    semestre = models.IntegerField(("semestre"))
    idUsuario = models.ForeignKey(User, verbose_name=("nombre de usuario"), on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.numControl)


class Aduedo(models.Model):
    numControl = models.ForeignKey(Alumno, verbose_name=("Alumno"), on_delete=models.CASCADE)
    creditosAcum = models.IntegerField(("creditos acumulados"))
    adeudo = models.BinaryField(("aduedo de libro"), default=0)
    cantMov = models.IntegerField(("cantidad de movilidades cursados"))
    cursoVerano = models.BinaryField(("curso de verano"))
    coment = models.CharField(("commentario"), max_length=320)
    matRC = models.IntegerField(("materias cursadando en RC"), default=0)
    eligible = models.BooleanField(("Es eligible"), default=False)


class Materia(models.Model):
    materia = models.CharField(("materia"), max_length=50)
    creditos = models.IntegerField(("creditos"))
    idInstituto = models.ForeignKey(Instituto, verbose_name=("id instituto"), on_delete=models.CASCADE)
    idCarrera  = models.ForeignKey(Carrera, verbose_name=("id carrera"), on_delete=models.CASCADE)

    def __str__(self):
        return self.materia


class MateriasDelAlumno(models.Model):
    numControl = models.ForeignKey(Alumno, verbose_name=("numero de control"), on_delete=models.CASCADE)
    idMaterias = models.ForeignKey(Materia, verbose_name=("materia"), on_delete=models.CASCADE)
    idInstituto = models.ForeignKey(Instituto, verbose_name=("instituto"), on_delete=models.CASCADE)
    idCarrera = models.ForeignKey(Carrera, verbose_name=("carrera"), on_delete=models.CASCADE)
    calif = models.DecimalField(("calificacion"), max_digits=5, decimal_places=2)


class ServicioEscolar(models.Model):
    nombre = models.CharField(("nombre"), max_length=50)
    apellido = models.CharField(("apellido"), max_length=50)
    coment = models.CharField(("comentario"), max_length=320)
    idUsuario = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Academia(models.Model):
    nombre = models.CharField(("nombre"), max_length=50)
    apellido = models.CharField(("apellido"), max_length=50)
    idUsuario = models.ForeignKey(User, verbose_name=("id usuario"), on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Status(models.Model):
    status = models.CharField(("status"), max_length=50)
    # status : enviado, pendiente, aceptado, rechazado
    tipoStatus = models.IntegerField(("tipo de status") ,default=1)
    descStat = models.CharField(("descripcion"), max_length=50)

    def __str__(self):
        return self.status  


class Solicitud(models.Model):
    fechaSolic = models.DateField(("fecha de registro"), auto_now=True, auto_now_add=False)
    coment = models.CharField(("comentario"), max_length=320)
    idInstituto = models.ForeignKey(Instituto, verbose_name=("instituto"), on_delete=models.CASCADE)
    numeroControl = models.ForeignKey(Alumno, verbose_name=("numero de control"), on_delete=models.CASCADE)
    idStatus = models.ForeignKey(Status, verbose_name=("status"), on_delete=models.CASCADE)
    idServicio = models.ForeignKey(ServicioEscolar, verbose_name=("id servicio escolar"), on_delete=models.CASCADE)
    idAcademia = models.ForeignKey(Academia, verbose_name=("id academia"), on_delete=models.CASCADE)

    def __str__(self):
        return self.coment 


class Movimiento(models.Model):
    idSolicitud = models.ForeignKey(Solicitud, verbose_name=("id solicitud"), on_delete=models.CASCADE)
    fecha = models.DateField(("fecha de movimiento"), auto_now=True, auto_now_add=False)
    usuario = models.ForeignKey(User, verbose_name=("id usuario"), on_delete=models.CASCADE)
    idStatus = models.ForeignKey(Status, verbose_name=("id status"), on_delete=models.CASCADE)


class MateriaSolicitada(models.Model):
    idSolicitud = models.ForeignKey(Solicitud, verbose_name=("id solicitud"), on_delete=models.CASCADE)
    idMateria = models.ForeignKey(Materia, verbose_name=("id materia"), on_delete=models.CASCADE)
    idInstituto = models.ForeignKey(Instituto, verbose_name=("id instituto"), on_delete=models.CASCADE)
    idCarrera = models.ForeignKey(Carrera, verbose_name=("id carrera"), on_delete=models.CASCADE)
    calif = models.DecimalField(("calificacion"), max_digits=5, decimal_places=2)