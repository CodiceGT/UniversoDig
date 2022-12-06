from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.





#Modelos para manejo de usuarios
class Cuenta(models.Model):
    tipo = models.CharField(max_length=25)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.usuario.username


@receiver(post_save, sender=User)
def crear_cuenta(sender, instance, created, **kwargs):
    if created:
        Cuenta.objects.create(usuario=instance)


@receiver(post_save, sender=User)
def guardar_cuenta(sender, instance, created, **kwargs):
    instance.cuenta.save()