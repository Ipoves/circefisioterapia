from django import forms
  
class FormularioContacto(forms.Form):
    
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class': 'campos-formulario'}), label="Nombre", required=True )
    apellido=forms.CharField(widget=forms.TextInput(attrs={'class': 'campos-formulario'}),label="Apellidos", required=True)
    telefono=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'campos-formulario'}), required=True)
    email=forms.CharField(widget=forms.TextInput(attrs={'class': 'campos-formulario'}), label="Email", required=True)
    contenido=forms.CharField(label="Preguntanos",required=True ,widget=forms.Textarea(attrs={'class': 'campos-formulario'}))


        
        
        