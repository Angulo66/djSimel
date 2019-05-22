from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib import messages

from django.db.models.base import ObjectDoesNotExist

# Create your views here.
from django.http import HttpResponse
from .models import Instituto, Solicitud
from .forms import SolicitudForm

"""
def get_template(request):
    try:
        if request.is_authenticated:
            if request.groups.get(name="Jefatura"):
                print("jefatura")
            else:
                print("no existes")
    except Exception:
        print(Exception)
"""


def escolares(request):
    if request.user.is_authenticated():
        template = 'escolares.html'
    else:
        template = 'register/login.html'

    return render(request, template)


def alumno(request):
    print("request:", request)
    return render(request, 'alumno.html')


def solicitud(request):
    form = SolicitudForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Solicitud Enviada!")
    else:
        messages.error(request, "Error en enviar Solicitud!")    
    context = {
        "form": form
    }
    template = 'solicitud.html'
    return render(request, template, context)

def solicitud_detail(request, id=None):
    instance = get_object_or_404(Solicitud, id=id)
    context = {
        "title": instance.numControl,
        "instance": instance 
    }
    return render(request, '', context)

def coordinacion(request):
    if request.user.is_authenticated():
        template = 'coordinacion.html'
    else:
        template = 'register/login.html'

    return render(request, template)


def jefatura(request):
    if request.user.is_authenticated():
        template = 'jefatura.html'
    else:
        template = 'register/login.html'

    return render(request, template)


def solicitudes(request):
    queryset = Solicitud.objects.all()
    context = {
        "object_list": queryset
    }
    template = 'solicitudes.html'
    return render(request, template, queryset)