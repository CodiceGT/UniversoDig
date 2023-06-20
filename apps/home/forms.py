from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'groups']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'groups']


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

class FormNuevoReporte(forms.ModelForm):
    class Meta:
        model = ReporteFallo
        fields = ['contratacion', 'descripcion', 'tecnico_asignado']