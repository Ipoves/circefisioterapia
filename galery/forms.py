from django.forms import ModelForm
from .models import Galery

class GaleryForm(ModelForm):
    
    class Meta:
        model = Galery
        
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'campos-formulario', 'placeholder': 'Nombre de la imagen'})
        self.fields['description'].widget.attrs.update({'class': 'campos-formulario'})
        self.fields['photo'].widget.attrs.update({'class': 'campos-formulario'})