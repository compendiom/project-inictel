from django import forms
from django.db import models
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField

# Create your models here.
class Curso:
    programa = models.CharField(max_length=255)
    nombreCurso = models.CharField(max_length=160)
    nota = models.CharField(max_length=5)
    horas = models.CharField(max_length=2)

class Persona(models.Model):
    nombre = models.CharField(max_length=160)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=11)

class Formulario(ModelForm):
    #apellido = forms.CharField(max_length=30, required=True, error_messages={'required': 'El apellido debe contener solo letras mayúsculas y espacios.'})
    #dni = forms.CharField(max_length=11, required=True, error_messages={'required':'El DNI debe tener exactamente 8 dígitos numéricos.'})
    class Meta:
        model = Persona
        fields = ('dni', 'apellido')
        labels = {
            'dni': 'Número de DNI'
        }
        widgets = {
            'dni': forms.TextInput(attrs={'type':'text', 'pattern':'.{8}', 'name': 'dni', 'placeholder': '12345678', 'title': 'Este campo debe tener 8 dígitos numéricos'}),
            'apellido': forms.TextInput(attrs={'type':'text', 'pattern':'[A-ZÑ]+', 'name': 'apellido', 'placeholder': 'PEREZ', 'title': 'Este campo debe tener letras mayúsculas'})
        }
    
    recaptcha = ReCaptchaField(
        public_key='6Lcjxg4qAAAAAM2PCbF_cI6LElkbajJjozp3pdaM',
        private_key='6Lcjxg4qAAAAALX_2GA1ujoolSi06sNEFKR3O33A',
        error_messages={'required': 'Debes seleccionar el captcha para poder conocer el resultado de la búsqueda que realizó'},
        required=True
    )