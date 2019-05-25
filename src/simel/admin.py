from django.contrib import admin
# Register your models here.
from django.db import models

from .models import (Academia, Aduedo, Alumno, Carrera, Coordinador, Estado,
                     Instituto, Jefatura, Localidad, Materia,
                     MateriasDelAlumno, MateriaSolicitada, Movimiento,
                     Municipio, Pais, Plan, ServicioEscolar, Solicitud, Status)

admin.AdminSite.site_header = "SIMEL ADMIN"


class AdeudoAdmin(admin.ModelAdmin):
    list_display = ('numControl','creditosAcum','cantMov','matRC','eligible')

class AdminAdmin(admin.ModelAdmin):
    list_display = ('idUsuario', 'nombre','apellido')

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','numControl','idCarrera','semestre')
    list_filter = ('idCarrera','semestre')

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre','especialidad','idInstituto')    

class InstitutoAdmin(admin.ModelAdmin):
    list_display = ('instituto', 'idLocalidad')

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('idCarrera','materia', 'creditos', 'idInstituto')
    list_filter = ('idCarrera',)

class MateriasAdmin(admin.ModelAdmin):
    list_display = ('idCarrera', 'numControl','idMaterias','calif','idInstituto')  
    list_filter = ('idCarrera',)

class MateriasSolAdmin(admin.ModelAdmin):
    list_display = ('idCarrera','idInstituto','idSolicitud','idMateria','calif')
    list_filter = ('idCarrera', 'idInstituto','idSolicitud')   

class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('coment', 'numeroControl','fechaSolic',)
    list_filter = ('idInstituto', 'idStatus','fechaSolic')
    date_hierarchy = ('fechaSolic')

admin.site.register(Plan)
admin.site.register(Carrera, CarreraAdmin)

admin.site.register(Coordinador, AdminAdmin)
admin.site.register(Academia, AdminAdmin)
admin.site.register(Jefatura, AdminAdmin)
admin.site.register(ServicioEscolar, AdminAdmin)

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(MateriasDelAlumno, MateriasAdmin)
admin.site.register(MateriaSolicitada, MateriasSolAdmin)

admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Movimiento)
admin.site.register(Status)
admin.site.register(Aduedo, AdeudoAdmin)

admin.site.register(Instituto, InstitutoAdmin)

admin.site.register(Localidad)
admin.site.register(Municipio)
admin.site.register(Estado)
admin.site.register(Pais)
