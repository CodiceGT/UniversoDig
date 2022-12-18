from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class RegistroServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class InformacionForm(forms.ModelForm):
    class Meta:
        model = Informacion
        fields = '__all__'
