from django.urls import path, include
from registro import views

urlpatterns = [
    path('', views.index, name='index'),
    # Clientes
    path('cliente/agregar/', views.agregarCliente, name='agregar-cliente'),
    path('cliente/listar/', views.listarClientes, name='lista-clientes'),
    path('cliente/enviar/', views.enviarCliente, name='enviar-cliente'),
    path('cliente/detalle/<int:id>/', views.detalleCliente, name='detalle-cliente'),
    path('cliente/editar/<int:id>/', views.editarCliente, name='editar-cliente'),
    path('cliente/actualizar/<int:id>/', views.actualizarCliente, name='actualizar-cliente'),
    path('cliente/eliminar/<int:id>/', views.eliminarCliente, name='eliminar-cliente'),
    # Visitas
    path('cliente/<int:id>/visita/agregar/', views.agregarVisita, name='agregar-visita'),
    path('cliente/<int:id>/visita/enviar/', views.enviarVisita, name='enviar-visita'),
    path('cliente/<int:id>/visita/listar/', views.listarVisitasPorCliente, name='lista-visitas-cliente'),
    path('cliente/<int:id_cliente>/visita/detalle/<int:id_visita>/', views.detalleVisita, name='detalle-visita'),
    path('cliente/<int:id_cliente>/visita/editar/<int:id_visita>/', views.editarVisita, name='editar-visita'),
    path('cliente/<int:id_cliente>/visita/actualizar/<int:id_visita>/', views.actualizarVisita, name='actualizar-visita'),
    path('cliente/<int:id_cliente>/visita/eliminar/<int:id_visita>/', views.eliminarVisita, name='eliminar-visita'),
    path('visita/listar/', views.listarVisitas, name='lista-visitas'),
]