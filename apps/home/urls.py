from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from UniversoDig import settings
from .views import login_view, LogoutView, usuarios_view, usuarionuevo_view, usuarios_filtrados, EditarUsuarioView, \
    usuarioeliminar_view, HomeView, ClienteListView, NuevoClienteView, BorrarClienteView, ModificarClienteView, \
    ServiciosView, NuevoServicioView, BorrarServicioView, ModificarServicioView, ContratacionesView, \
    NuevaContratacionView, BorrarContratacionView, ModificarContratacionView, PagosView, NuevoRecibo, NuevoDetalle, \
    borrar_detalle_pago_view, informacionempresa_view, InformacionView, BorrarInformacionView, ModificarInformacionView, \
    reporte_fallo, cambiar_estado_reporte_fallo_view, cambiar_tecnico_reporte_fallo_view, borrar_reporte_fallos_view, \
    ReporteExcel, ReporteContrataciones, ReciboPDFView, template_view

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

                  # Pagos
                  path('pagos/', PagosView, name='pagos'),
                  path('recibo/', NuevoRecibo, name='nuevorecibo'),
                  path('detallepago/<int:pk>', NuevoDetalle, name='nuevodetalle'),
                  path('detalle/borrar/<int:pk>', borrar_detalle_pago_view, name='borrar_detalle_pago'),

                  # Información de empresa
                  path('informacion/', informacionempresa_view, name='informacion'),
                  path('informacion/nueva/', InformacionView, name='nuevainformacion'),
                  path('informacion/borrar/<int:pk>', BorrarInformacionView, name='borrarinformacion'),
                  path('informacion/editar/<int:pk>', ModificarInformacionView.as_view(), name='modificarinformacion'),

                  path('reportes/', reporte_fallo, name='reportes'),
                  path('reportes/cambiarestado/<int:pk>/<str:estado>', cambiar_estado_reporte_fallo_view,
                       name='cambiarestado_reporte'),
                  path('reportes/cambiartecnico/<int:id_reporte>/<int:id_tecnico>', cambiar_tecnico_reporte_fallo_view,
                       name='cambiartecnico_reporte'),
                  path('reportes/eliminar/<int:id_reporte>', borrar_reporte_fallos_view,
                       name='borrar_reporte'),

                  path('reporte', ReporteExcel.as_view(), name='reporteClientes'),
                  path('reporte/contratacion', ReporteContrataciones.as_view(), name='reporteContratacion'),

                  # Facturas PDF
                  path('recibopdf/<int:pk>', ReciboPDFView.as_view(), name='recibopdf'),
                  
                  path('template/', template_view, name='template')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
