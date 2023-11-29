from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Contratacion)
admin.site.register(Recibo)
admin.site.register(DetallePago)
admin.site.register(Sucursal)
admin.site.register(ReporteFallo)