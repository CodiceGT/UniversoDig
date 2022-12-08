"""UniversoDig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.home import views
from .views import *

app_name='home'

urlpatterns = [
    #Inicio y cierre de sesión
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),

    #Dashboard
    path('', HomeView, name='home'),
    path('clientes/', ClientesView, name='clientes'),
    path('clientes/nuevo/', NuevoClienteView, name='nuevocliente'),
    path('servicios/', ServiciosView, name='servicios'),
    path('servicios/nuevo/', NuevoServicioView, name='nuevoservicio'),
]