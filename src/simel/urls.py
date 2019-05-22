from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('tablero', views.tablero, name='tablero'),
    path('solicitud', views.solicitud, name='solicitud'),
    path('solicitudes', views.solicitudes, name='solicitudes')
]