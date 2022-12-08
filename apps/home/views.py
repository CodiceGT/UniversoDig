from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render, redirect

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