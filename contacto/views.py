from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
import logging
from .forms import FormularioContacto



# Create your views here.
logger = logging.getLogger(__name__)

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            
            asunto="Mensaje de un usuario desde la WEB de CIRCE"
            email_desde=settings.EMAIL_HOST_USER
            destino = settings.EMAIL_HOST_USER
            destinatario=[destino]
            
            mensaje=request.POST.get("contenido")
            nombre=request.POST.get("nombre")            
            apellido=request.POST.get("apellido")            
            telefono=request.POST.get("telefono")            
            email_usuario=request.POST.get("email")
            
            mensajeFinal = f"El usuario: {nombre}, {apellido} \n  Tlfn: {telefono} \nCon email: {email_usuario} \n Nos escribe lo siguiente: \n {mensaje}"

            try:
                send_mail(asunto, mensajeFinal, email_desde, destinatario)                
                messages.success(request, 'Correo enviado con exito.')
                return redirect('contacto')

            except BadHeaderError:
                messages.success(request, 'Ha habido un error en tu envio por favor revisa los datos y envíalo de nuevo Gracias.')
                return redirect('contacto')

            except Exception as e:
                logger.error(f"Error enviando correo: {e}")
                messages.success(request, f'Ocurrió un error enviando el correo: {e}')
                return redirect('contacto')
                

    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})