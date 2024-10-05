from django.shortcuts import render
from galery.models import Galery

def index(request):
    imagenes = Galery.objects.all()
    return render(request, 'index.html', {"imagenes":imagenes})

def tratamientos(request):
    return render(request, 'tratamientos/tratamientos.html', {})

def aviso(request):
    return render(request, 'aviso/aviso.html', {})