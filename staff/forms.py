from django.forms import ModelForm
from .models import Staff

class StaffForm(ModelForm):
    
    class Meta:
        model = Staff
        
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'campos-formulario', 'placeholder': 'Nombre de la imagen'})
        self.fields['last_name'].widget.attrs.update({'class': 'campos-formulario'})
        self.fields['description'].widget.attrs.update({'class': 'campos-formulario'})
        self.fields['photo'].widget.attrs.update({'class': 'campos-formulario'})
        