from datetime import date
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from .choices import ANIO_CHOICES, MES_CHOICES

# Create your models here.


class Cliente(models.Model):
    cui = models.CharField(max_length=13, null=True, blank=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    direccion = models.CharField(max_length=128)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=45, null=True, blank=True)
    usuario_registro = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Servicio(models.Model):
    tipo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=45)
    ancho_banda = models.CharField(max_length=45, null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    usuario_registro = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    direccion = models.CharField(max_length=255, null=True, default='')
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ultimo_pago = models.DateTimeField(default=date.today)
    # Estados: d=al dia, p=pendiente de pago, c=cancelado,
    estado = models.CharField(
        max_length=1, choices=ESTADO_CHOICES, default='D')
    usuario_registro = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s' % (self.pk, self.cliente, self.servicio)


class Recibo(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    contratacion = models.ForeignKey(Contratacion, on_delete=models.CASCADE)
    usuario_registro = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s %s' % (self.fecha.date(), self.pk, self.contratacion.pk, self.total)


class DetallePago(models.Model):
    mes = models.CharField(max_length=2, choices=MES_CHOICES)
    anio = models.CharField(max_length=4, choices=ANIO_CHOICES)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s Q%s' % (self.recibo, self.mes, self.anio, self.subtotal)


@receiver(pre_delete, sender=DetallePago)
def recalcular_total_recibo(sender, instance, **kwargs):
    recibo = instance.recibo
    recibo.total -= instance.subtotal
    recibo.save()


class Sucursal(models.Model):
    nombre = models.CharField(max_length=45)
    logo = models.ImageField(upload_to='logo', blank=True)
    direccion = models.CharField(max_length=128)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.direccion, self.telefono)


# models.py
class CustomUser(AbstractUser):
    # Agrega campos adicionales que necesitas
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, blank=True, null=True)

    # Puedes agregar más campos según tus necesidades

    def __str__(self):
        # O cualquier otro campo que desees mostrar como representación de usuario
        return self.username


class ReporteFallo(models.Model):
    ESTADO_CHOICES = (
        ('P', 'Pendiente'),
        ('E', 'En progreso'),
        ('S', 'Solucionado'),
    )
    contratacion = models.ForeignKey(Contratacion, on_delete=models.CASCADE)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=256)
    estado = models.CharField(
        max_length=1, choices=ESTADO_CHOICES, default='P')
    tecnico = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reporte de fallo #{self.id} - Cliente: {self.contratacion.cliente}"
