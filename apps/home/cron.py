from datetime import datetime, timedelta
from home.models import Contratacion
from home.views import actualizar_pendiente

def actualizar_pendientes_pago():
    contrataciones = Contratacion.objects.exclude(estado='C')
    for contratacion in contrataciones:
        actualizar_pendiente(contratacion)