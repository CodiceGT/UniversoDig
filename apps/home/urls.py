from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from UniversoDig import settings
from .views import *

app_name = 'home'

urlpatterns = [
                  # Inicio y cierre de sesión
                  path('login/', login_view, name='login'),
                  path('logout/', LogoutView, name='logout'),

                  # cuentas
                  path('usuarios/', usuarios_view, name='usuarios'),
                  path('usuarios/nuevo/', usuarionuevo_view, name='usuario_nuevo'),
                  path('usuarios/filtrado/', usuarios_filtrados, name='usuario_filtrado'),
                  path('usuarios/editar/<int:pk>', EditarUsuarioView.as_view(), name='usuario_editar'),
                  path('usuarios/eliminar/<str:username>', usuarioeliminar_view, name='usuario_eliminar'),

                  # Dashboard
                  #TODO corregir estas dos rutas
                  path('', HomeView, name='home'),
                  path('dashboard/', HomeView, name='home'),
                  path('clientes/', ClienteListView.as_view(), name='clientes'),
                  path('clientes/nuevo/', NuevoClienteView, name='nuevocliente'),
                  path('clientes/borrar/<int:pk>', BorrarClienteView, name='borrarcliente'),
                  path('clientes/editar/<int:pk>', ModificarClienteView.as_view(), name='modificarcliente'),

                  # Servicios
                  path('servicios/', ServiciosView, name='servicios'),
                  path('servicios/nuevo/', NuevoServicioView, name='nuevoservicio'),
                  path('servicios/borrar/<int:pk>', BorrarServicioView, name='borrarservicio'),
                  path('servicios/editar/<int:pk>', ModificarServicioView.as_view(), name="modificarservicio"),

                  # Contrataciones
                  path('contrataciones/', ContratacionesView, name='contrataciones'),
                  path('contrataciones/nuevo/', NuevaContratacionView, name='nuevacontratacion'),
                  path('contrataciones/borrar/<int:pk>', BorrarContratacionView, name='borrarcontratacion'),
                  path('contratacion/editar/<int:pk>', ModificarContratacionView.as_view(),
                       name='modificarcontratacion'),

               # Contrataciones API
               # URL para listar contrataciones (método GET)
               path('contrataciones_api/', ContratacionAPIView.as_view(), name='listar_contrataciones'),
               path('contrataciones_api/nueva/', ContratacionAPIView.as_view(), name='nueva_contratacion_ajax'),
               path('dashboard/actualiar_pagos', actualizar_pendientes_pagos_view, name='actualizar_pendiente_pago'),
               
                  # Pagos
                  path('pagos/', PagosView, name='pagos'),
                  path('recibo/', NuevoRecibo, name='nuevorecibo'),
                  path('detallepago/<int:pk>', NuevoDetalle, name='nuevodetalle'),
                  path('detalle/borrar/<int:pk>', borrar_detalle_pago_view, name='borrar_detalle_pago'),

                  # Información de empresa
                  path('sucursal/', sucursalempresa_view, name='sucursal'),
                  path('sucursal/nueva/', SucursalView, name='nuevasucursal'),
                  path('sucursal/borrar/<int:pk>', BorrarSucursalView, name='borrarsucursal'),
                  path('sucursal/editar/<int:pk>', ModificarSucursalView.as_view(), name='modificarsucursal'),

                  path('reportes/', reporte_fallo, name='reportes'),
                  path('reportes/cambiarestado/<int:pk>/<str:estado>', cambiar_estado_reporte_fallo_view,
                       name='cambiarestado_reporte'),
                  path('reportes/cambiartecnico/<int:id_reporte>/<int:id_tecnico>', cambiar_tecnico_reporte_fallo_view,
                       name='cambiartecnico_reporte'),
                  path('reportes/eliminar/<int:id_reporte>', borrar_reporte_fallos_view,
                       name='borrar_reporte'),
                  
                  path('template/', template_view, name='template')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
