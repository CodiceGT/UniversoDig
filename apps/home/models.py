from datetime import date
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.
class Cliente(models.Model):
    cui = models.CharField(max_length=13, null=True, blank=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    direccion = models.CharField(max_length=128)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=45, null=True, blank=True)
    creacion = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre + " " +self.apellido


class Servicio(models.Model):
    tipo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=45)
    ancho_banda = models.CharField(max_length=45, null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    creacion = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '%s %s' % (self.tipo, self.nombre)


class Contratacion(models.Model):
    ESTADO_CHOICES = (
        ('D', 'Al día'),
        ('P', 'Pendiente'),
        ('C', 'Cancelado'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=128)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ultimo_pago = models.DateTimeField(default=date.today)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='D') # Estados: d=al dia, p=pendiente de pago, c=cancelado,
    creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s' % (self.pk, self.cliente, self.servicio)


class Recibo(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    contratacion = models.ForeignKey(Contratacion, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s %s' % (self.fecha.date(), self.pk, self.contratacion.pk, self.total)


class ReporteFallo(models.Model):
    ESTADO_CHOICES = (
        ('P', 'Pendiente'),
        ('E', 'En progreso'),
        ('S', 'Solucionado'),
    )
    contratacion = models.ForeignKey(Contratacion, on_delete=models.CASCADE)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=256)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='P')
    tecnico_asignado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reportes_asignados')

    def __str__(self):
        return f"Reporte de fallo #{self.id} - Cliente: {self.contratacion.cliente}"


#Modelos de meses y años para control de pagos
#Año
class Anio(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return '%s' % (self.numero)


class Mes(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % (self.nombre)


class DetallePago(models.Model):
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s Q%s' % (self.recibo, self.mes, self.anio, self.subtotal)

class Informacion(models.Model):
    nombre = models.CharField(max_length=45)
    logo = models.ImageField(upload_to='logo', default='descarga.png')
    direccion = models.CharField(max_length=128)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.direccion, self.telefono)