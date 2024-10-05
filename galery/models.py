from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
import os

# Create your models here.
class Galery(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='imagenes/galeria/',blank=False, null=False)
    
    class Meta: 
        verbose_name='Galeria'
        verbose_name_plural='Galeria'
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
    # Guardar la referencia al archivo original antes de actualizar
        try:
            this = Galery.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except:
            pass  # En el primer guardado (cuando el objeto aún no existe) no hay imagen previa
        super().save(*args, **kwargs)
    
@receiver(post_delete, sender=Galery)
def eliminar_archivo_imagen(sender, instance, **kwargs):

    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)
    