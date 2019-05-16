from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('alumno', views.alumno, name='alumno'),
    path('coordinacion', views.coordinacion, name="coordinacion"),
    path('jefatura', views.jefatura, name="jefatura"),
    path('escolares', views.escolares, name="escolares")
]