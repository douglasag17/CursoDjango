from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime
from Proyecto1.Objects.persona import Persona

def saludar(request):
    p1 = Persona('Douglas', 'Ardila')
    fechaActual = datetime.datetime.now()
    temas = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']

    argsCtx = {'nombre': p1.nombre, 'apellido': p1.apellido, 
               'horaActual': fechaActual.time, 'fechaActual': fechaActual.date,
               'temas': temas}

    return render(request, 'saludar.html', argsCtx)

def despedir(request):
    return render(request, 'despedir.html')

def darFecha(request):
    fechaActual = datetime.datetime.now()
    argsCtx = {'fechaActual': fechaActual}
    return render(request, 'fecha.html', argsCtx)