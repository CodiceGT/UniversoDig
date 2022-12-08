from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
