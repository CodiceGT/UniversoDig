
from django.views.generic import ListView, CreateView
from .forms import ClienteForm
from .models import Cliente
from django.urls import reverse_lazy

# Create your views here.

# Registrar Clientes
class CrearClienteView(CreateView):
    template_name='FormClientes.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente')


#Listar clientes 
class ListarCliente(ListView):
    template_name = 'Cliente.html'
    model = Cliente

    def get_queryset(self):
        return Cliente.objects.all()


