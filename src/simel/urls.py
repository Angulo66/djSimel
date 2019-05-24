from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('tablero', views.tablero, name='tablero'),
    path('solicitudes', views.solicitudes, name='solicitudes'),
    path('servicio', views.servicio, name='servicio')
]


# Materia Solicitada Mixins

urlpatterns += [
    path('materia', views.MateriaSolicitadaListView.as_view(), name='materia_changelist'),
    path('materia/add', views.MateriaSolicitdadCreateView.as_view(), name='materia_add'),
    path('materia/<int:pk>', views.MateriaSolicitdadUpdateView.as_view(), name='materia_change')
]

# Solicitud Mixins

urlpatterns += [
    path('solicitud', views.SolicitudListView.as_view(), name='solicitud_changelist'),
    path('solicitud/add', views.SolicitudCreateView.as_view(), name='solicitud_add'),
    path('solicitud/<int:pk>', views.SolicitudUpdateView.as_view(), name='solicitud_change')
]

# Materias Solicitadas