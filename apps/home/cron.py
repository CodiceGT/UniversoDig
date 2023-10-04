from datetime import datetime, timedelta
from .models import Contratacion

def actualizar_pendientes_pago():
    """
    Es para todas las contrataciones excepto los que se dan de baja o cancelados
    """
    contrataciones = Contratacion.objects.exclude(estado='C')
    for contratacion in contrataciones:
        actualizar_pendiente(contratacion)


def actualizar_pendiente(contratacion):
    """
    Aplica para una contratación en específico

    Args:
        contratacion (_type_): _description_
    """
    dias_ultimo_pago = datetime.now().astimezone(contratacion.ultimo_pago.tzinfo) - contratacion.ultimo_pago
    # Verifica si tiene más de 30 días el último pago para sumarle a su saldo pendiente
    if dias_ultimo_pago.days >= 30:
        meses = dias_ultimo_pago / 30
        contratacion.saldo = meses.days * contratacion.servicio.costo
        contratacion.estado = 'P'  # Establece como "Pendiente de pago"
    else:
        contratacion.saldo = 0
        contratacion.estado = 'D'  # Establece como "Al día"
    contratacion.save()