from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Sum
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


'''def ClientesView(request):
    return render(request, 'Clientes.html')
'''
# Vista Para Registrar Clientes
@login_required
def NuevoClienteView(request):
    cui = request.POST['cui']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    correo = request.POST['correo']
    
    cliente = Cliente(cui=cui, nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, correo=correo)
    cliente.save()
    
    return redirect('home:clientes')

#Vista Para Listar Clientes
def ListarCliente(request):
    return render(request, 'Clientes.html', {'clientes':Cliente.objects.all()})

#Vista Para Borrar Clientes
def BorrarClienteView(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('home:clientes')

#Vista Para Modificar Clientes
class ModificarClienteView(UpdateView):
    template_name = 'modificarCliente.html'
    model = Cliente
    fields = ['cui', 'nombre', 'apellido', 'direccion', 'telefono', 'correo']
    success_url = reverse_lazy('home:clientes')

#Vista Para Listar usuarios
def UsuarioView(request):
    model = User
    return render(request, 'cuentas.html', {'usuarios':User.objects.all()})

#Vistas para listar servicios
def ServiciosView(request):
    return render(request, 'servicios.html', {'servicios':Servicio.objects.all()})

#Vista para insertar servicios
def NuevoServicioView(request):
    tipo = request.POST['tipo']
    nombre = request.POST['nombre']
    ancho_banda = request.POST['ancho_banda']
    costo = request.POST['costo']
    servicio = Servicio(tipo=tipo, nombre=nombre, ancho_banda=ancho_banda, costo=costo)
    servicio.save()
    return redirect('home:servicios')


#Vista para borrar servicios
def BorrarServicioView(request, pk):
    servicio = Servicio.objects.get(pk=pk)
    servicio.delete()
    return redirect('home:servicios')

#Vista para modificar servicios
class ModificarServicioView(UpdateView):
    template_name = 'modificarServicio.html'
    model = Servicio
    fields = ['tipo', 'nombre', 'ancho_banda', 'costo']
    success_url = reverse_lazy('home:servicios')


#Vista para listar contrataciones
def ContratacionesView(request):
    return render(request, 'contrataciones.html', {
        'contrataciones':Contratacion.objects.all(),
        'clientes':Cliente.objects.all(),
        'servicios':Servicio.objects.all()
        })


#Vista para crear una contratacion
def NuevaContratacionView(request):
    cliente = Cliente.objects.get(pk=(request.POST['cliente']))
    servicio = Servicio.objects.get(pk=(request.POST['servicio']))
    direccion = request.POST['direccion']
    contratacion = Contratacion(cliente=cliente, servicio=servicio, direccion=direccion)
    contratacion.save()
    return redirect('home:contrataciones')


#Vista para borrar contratacion
def BorrarContratacionView(request, pk):
    contratacion = Contratacion.objects.get(pk=pk)
    contratacion.delete()
    return redirect('home:contrataciones')

#Vista para modificar contratacion
class ModificarContratacionView(UpdateView):
    template_name = 'modificarContratacion.html'
    model = Contratacion
    fields = ['cliente', 'servicio', 'direccion']
    success_url = reverse_lazy('home:contrataciones')

#Vista para listar pagos
def PagosView(request):
    return render(request, 'pagos.html', {'pagos':Recibo.objects.all().order_by('-pk'), 'contrataciones':Contratacion.objects.all()})

#Vista para listar informacion de empresa
def ListarInformaciónView(request):
     return render(request, 'informacion.html', {'informacion':Informacion.objects.all()})

#Vista para registrar informacion de empresa
def InformacionView(request):
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']

    informacion = Informacion(nombre=nombre, direccion=direccion, telefono=telefono)
    informacion.save()
    return redirect('home:informacion')

#Vista para borrar informacion de empresa
def BorrarInformacionView(request, pk):
    informacion = Informacion.objects.get(pk=pk)
    informacion.delete()
    return redirect('home:informacion')

#Vista para modificar informacion de empresa
class ModificarInformacionView(UpdateView):
    template_name = 'modificarInformacion.html'
    model = Informacion
    fields = ['nombre', 'direccion', 'telefono']
    success_url = reverse_lazy('home:informacion')

def NuevoRecibo(request):
    pk = request.POST['contratacion']
    contratacion = Contratacion.objects.get(pk=pk)
    recibo = Recibo(contratacion=contratacion, total=0)
    recibo.save()
    return render(request, 'recibo.html', {'contratacion':contratacion, 'recibo':Recibo.objects.last(), 'meses':Mes.objects.all(), 'anios':Anio.objects.all()})

def NuevoDetalle(request, pk):
    recibo = pk
    mes = request.POST.get('mes', '')
    anio = request.POST.get('anio', '')
    subtotal = request.POST.get('subtotal','')

    valido = False #Variable que sirve para verificar si ese mes ya está pagado.

    recibo = Recibo.objects.get(pk=recibo)
    contratacion = Contratacion.objects.get(pk=recibo.contratacion.id)

    if mes != '' and anio != '' and subtotal != '':
        if Mes.objects.filter(nombre=mes).count() == 0:
            mes = Mes(nombre=mes)
            mes.save()
            mes = Mes.objects.last()
        else:
            mes = Mes.objects.get(nombre=mes)
        
        if Anio.objects.filter(numero=anio).count() == 0:
            anio = Anio(numero=anio)
            anio.save()
            anio = Anio.objects.last()
        else:
            anio = Anio.objects.get(numero=anio)

        for recibito in Recibo.objects.filter(contratacion=contratacion).iterator():
            if DetallePago.objects.filter(recibo=recibito, mes=mes, anio=anio).count() != 0:
                valido = True
                
        if valido != True:
            detallepago = DetallePago(mes=mes, anio=anio, subtotal=subtotal, recibo=recibo)
            detallepago.save()

        recibo.total = DetallePago.objects.filter(recibo=recibo).aggregate(Sum('subtotal'))['subtotal__sum']
        if recibo.total is None:
            recibo.total = 0
        recibo.save()
        


    return render(request, 'recibo.html', {'contratacion':contratacion, 'recibo':recibo, 'meses':Mes.objects.all(), 'anios':Anio.objects.all()})
