from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from django.http import HttpResponse
from .models import Instituto
from .forms import LoginForm

def simel(request):
    return render(request, 'registration/login.html')

def escolares(request):
    return render(request, 'escolar.html')

def alumno(request):
    return render(request, 'alumno.html')

def solicitud(request):
    return render(request, 'solicitud.html')

def coordinacion(request):
    return render(request, 'coordinacion.html')

def jefatura(request):
    return render(request, 'jefatura.html')

def solicitudes(request):
    return render(request, 'solicitudes.html')