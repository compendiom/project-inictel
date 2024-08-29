from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

# Create your models here.
class PersonaForm(forms.Form):
    
    tipo_documento = {
        ('24', 'Certificado'),
        ('25', 'Constancia')
    }
    
    
    apellido = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'pattern': '[A-ZÑ]+',
            'name': 'apellido',
            'placeholder': 'ex.: PEREZ',
            'title': 'Este campo debe tener SOLO letras mayúsculas',
            'required': 'true'
        })
    )

    dni = forms.CharField(
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'pattern': '[0-9]{8}',
            'name': 'dni',
            'placeholder': 'ex.: 12345678',
            'title': 'Este campo debe tener 8 dígitos numéricos',
            'required': 'true'
        })
    )

    codigo = forms.CharField(
        max_length=9,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'pattern': '[0-9]{5}',
            'name': 'codigo',
            'placeholder': 'ex.: 12345',
            'title': 'Este campo debe tener exactamente 5 dígitos numéricos',
            'required': 'true'
        })
    )

    tipo = forms.ChoiceField(
        choices=tipo_documento,
        widget=forms.RadioSelect(attrs={
            'class': 'form-control'
        }),
        required=True
    )