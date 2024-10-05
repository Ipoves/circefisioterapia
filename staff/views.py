from django.shortcuts import render
from .models import Staff


# Create your views here.
def staff(request):
    
    personal = Staff.objects.all()
    
    return render(request, 'personal/personal.html', {"personal":personal})

