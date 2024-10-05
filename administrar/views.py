from django.shortcuts import render, redirect,get_object_or_404
from staff.models import Staff
from staff.forms import StaffForm
from galery.forms import GaleryForm
from galery.models import Galery
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def administrar(request):
    
    return render(request, 'administrar/administrar.html', {})

def equipo(request):
    
    personal = Staff.objects.all()
    
    return render(request, 'administrar/equipo.html', {'personal':personal})

def edit(request, id):
    personal = Staff.objects.get(id=id)
    
    if request.method == 'GET':
        form = StaffForm(instance= personal)
        context = {
            'form': form,
            'id' : id
        }       
        return render(request, 'administrar/edit.html',context)
    
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance= personal)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id' : id
        }    
        messages.success(request, 'Editado con exito.')
        return redirect('equipo')

    
def create(request):
    if request.method == 'GET':
        form = StaffForm()
        context = {
            'form': form
        }           
        return render(request, 'administrar/create.html',context)
    
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Creado con Exito.')
        return redirect('equipo')
        
    
@require_POST
def delete(request, id):
    elemento = get_object_or_404(Staff, pk=id)
    elemento.delete()    
    messages.success(request, 'Eliminado con Exito.')
    return redirect('equipo')

def galeria(request):  
    imagenes = Galery.objects.all()   
    return render(request, 'administrar/galeria.html', {'imagenes':imagenes})

@require_POST
def delete_galeria(request, id):
    elemento = get_object_or_404(Galery, pk=id)
    elemento.delete()
    messages.success(request, 'Eliminado con Exito.')
    return redirect('galeria')

def edit_galeria(request, id):
    imagen = Galery.objects.get(id=id)
    
    if request.method == 'GET':
        form = GaleryForm(instance= imagen)
        context = {
            'form': form,
            'id' : id
        }       
        return render(request, 'administrar/edit-galeria.html',context)
    
    if request.method == 'POST':
        form = GaleryForm(request.POST, request.FILES, instance= imagen)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id' : id
        }  
        messages.success(request, 'Imagen editada con exito.')         
        return redirect('galeria')

    
def create_galeria(request):
    if request.method == 'GET':
        form = GaleryForm()
        context = {
            'form': form
        }           
        return render(request, 'administrar/create-galeria.html',context)
    
    if request.method == 'POST':
        form = GaleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Añadido con Exito.')
        return redirect('galeria')
    
def cerrar_sesion(request):
    
    logout(request)
    return redirect('index')

def logear(request):
    
    if request.method == "POST":
        form=AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrase = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contrase)
            if usuario is not None:
                login(request, usuario)
                return redirect('index')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")
                       
    form = AuthenticationForm()
    return render(request, "administrar/login.html", {"form":form})
    
        
