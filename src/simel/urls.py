from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('tablero', views.tablero, name='tablero'),
    path('solicitud', views.solicitud, name='solicitud'),
    path('solicitudes', views.solicitudes, name='solicitudes'),
    path('servicio', views.servicio, name='servicio')
]

urlpatterns += [
    path('simel/solicita',views.create_solicitud, name='solicita_post'),
]

# Materia Solicitada Mixins

urlpatterns += [
    path('materia', views.MateriaSolicitadaListView.as_view(), name='materia_changelist'),
    path('materia/add', views.MateriaSolicitdadCreateView, name='materia_add'),
    path('materia/<int:pk>', views.MateriaSolicitdadUpdateView.as_view(), name='materia_change')
]



# Solicitud Mixins
"""
urlpatterns += [
    path('solicitud/add', views.SolicitudCreateView.as_view(), name='solicitud_add'),
    path('solicitud/<int:pk>', views.SolicitudUpdateView.as_view(), name='solicitud_change')
]
"""
