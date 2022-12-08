from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.

#Vistas para inicio y cierre de sesión
class LoginView(LoginView):
    template_name = 'registration/login.html'


@login_required
def HomeView(request):
    return render(request, 'index.html')


def LogoutView(request):
    logout(request)
    return redirect('home:login')


#Vista para Dashboard

# Registrar Clientes
class CrearClienteView(CreateView, ListView):
    template_name='Clientes.html'
    form_class = ClienteForm
    success_url = reverse_lazy('home:clientes')
    model = Cliente

    def get_queryset(self):
        return Cliente.objects.all()
    

    

#Vistas personalizadas
def ServiciosView(request):
    return render(request, 'servicios.html')


def NuevoServicioView(request):
    tipo = request.POST['tipo']
    nombre = request.POST['nombre']
    ancho_banda = request.POST['ancho_banda']
    costo = request.POST['costo']

    servicio = Servicio(tipo=tipo, nombre=nombre, ancho_banda=ancho_banda, costo=costo)
    servicio.save()

    return redirect('home:servicios')
