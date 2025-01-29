from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_proyectos, name='proyectos'),
    path('crear', views.proyecto_create, name='proyecto_create'),
    path('editar/<int:proyecto_id>/', views.proyecto_update, name='editar_proyecto'),
    path('eliminar/<int:proyecto_id>/', views.proyecto_delete, name='eliminar_proyecto'),
    path('proyectos/<int:proyecto_id>/', views.proyecto_detalle, name='proyecto_detalle'),
]