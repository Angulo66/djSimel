from django.contrib import admin

# Register your models here.

from django.db import models

from .models import (
    Usuario, Plan, Carrera, Alumno,
    Estado, Pais, Municipio, Localidad,
    Instituto, Materia, MateriasDelAlumno,
    ServicioEscolar, Academia, MateriaSolicitada,
    Status, Solicitud, Movimiento, Jefatura,
    Coordinador, Aduedo
    )

admin.site.register(Usuario)

admin.site.register(Plan)
admin.site.register(Carrera)

admin.site.register(Coordinador)
admin.site.register(Academia)
admin.site.register(Jefatura)
admin.site.register(ServicioEscolar)

admin.site.register(Alumno)
admin.site.register(Materia)
admin.site.register(MateriasDelAlumno)
admin.site.register(MateriaSolicitada)

admin.site.register(Solicitud)
admin.site.register(Movimiento)
admin.site.register(Status)
admin.site.register(Aduedo)

admin.site.register(Instituto)

admin.site.register(Localidad)
admin.site.register(Municipio)
admin.site.register(Estado)
admin.site.register(Pais)