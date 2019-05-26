from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('tablero', views.tablero, name='tablero'),
]

urlpatterns += [
    path('solicitud', views.solicitud, name='soliciutd'),
    path('solicitudes', views.solicitudes, name='solicitudes'),
    path('solicitud/sent', views.solicitudEnviado, name='solicitud_sent'),
    path('solicitud/status', views.solicitudStatus, name='solicitud_status')
]


urlpatterns += [
    path('simel/solicita',views.create_solicitud, name='solicita_post'),
]


# Actualizar
urlpatterns += [
    path('simel/actualiza',views.modificarSolicitud, name='modifica_post'),
]

# Materia Solicitada Mixins
urlpatterns += [
    path('materia', views.MateriaSolicitadaListView.as_view(), name='materia_changelist'),
    path('materia/add', views.MateriaSolicitdadCreateView, name='materia_add'),
    path('materia/<int:pk>', views.MateriaSolicitdadUpdateView.as_view(), name='materia_change')
]

# Escolares
urlpatterns += [
    path('capturas', views.capturarView, name='capturar_list'),
    path('capturas/<int:pk>', views.capturarUpdate, name='capturar_form')
]

# Academia
urlpatterns += [
    path('convalidar', views.convalidarView, name='convalidar_list')
]


# Solicitud Mixins
"""
urlpatterns += [
    path('solicitud/add', views.SolicitudCreateView.as_view(), name='solicitud_add'),
    path('solicitud/<int:pk>', views.SolicitudUpdateView.as_view(), name='solicitud_change')
]
"""
