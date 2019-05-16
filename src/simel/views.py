from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def login(request):
    return HttpResponse("login de simel")

def escolares(request):
    return HttpResponse("Escolares")

def alumno(request):
    return HttpResponse("alumno")

def coordinacion(request):
    return HttpResponse("coordinacion")

def jefatura(request):
    return HttpResponse("jefatura")    