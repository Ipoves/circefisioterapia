from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
import os

# Create your models here.
class Staff(models.Model):
    
    NOMBRE_CHOICES = (
    ('fisioterapeuta', 'Fisioterapeuta'),
    ('podologo', 'Podólogo'),
    ('rehabilitador', 'Rehabilitador'),
    ('psicologo', 'Psicólogo'),
    ('pilates', 'Pilates'),
    ('socio', 'Socio'),
    )
    
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    photo = models.ImageField(upload_to='imagenes/personal/',blank=True, null=True)
    
    especialidades = models.CharField(max_length=255, choices=NOMBRE_CHOICES, blank=False, null=False, default='fisioterapeuta')
    
    class Meta: 
        verbose_name='Personal'
        verbose_name_plural='Personal'
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
    # Guardar la referencia al archivo original antes de actualizar
        try:
            this = Staff.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except:
            pass  # En el primer guardado (cuando el objeto aún no existe) no hay imagen previa
        super().save(*args, **kwargs)
    
@receiver(post_delete, sender=Staff)
def eliminar_archivo_imagen(sender, instance, **kwargs):

    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)
    
    