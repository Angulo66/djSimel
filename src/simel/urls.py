from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('alumno', views.alumno, name='alumno'),
    path('coordinacion', views.coordinacion, name="coordinacion"),
    path('jefatura', views.jefatura, name="jefatura"),
    path('escolares', views.escolares, name="escolares"),
    path('solicitud', views.solicitud, name="solicitud"),
    path('solicitudes', views.solicitudes, name="solicitudes")
]

