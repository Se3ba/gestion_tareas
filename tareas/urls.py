from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/categoria/<int:categoria_id>/', views.tareas_por_categoria, name='tareas_por_categoria'),
]
