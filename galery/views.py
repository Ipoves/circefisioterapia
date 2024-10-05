from django.shortcuts import render
from .models import Galery
# Create your views here.
def galery(request):
    
    imagenes = Galery.objects.all()
    
    return render(request, 'galery/galery.html', {"imagenes":imagenes})