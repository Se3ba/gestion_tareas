import pytest
from tareas.models import Usuario, Tarea

@pytest.mark.django_db
def test_usuario_creacion():
    usuario = Usuario.objects.create(nombre='Juan', email='juan@example.com')
    assert usuario.nombre == 'Juan'
    assert usuario.email == 'juan@example.com'

@pytest.mark.django_db
def test_tarea_creacion():
    # Crear un usuario primero para asociarlo con la tarea
    usuario = Usuario.objects.create(nombre='Juan', email='juan@example.com')

    # Crear una tarea asociada a este usuario
    tarea = Tarea.objects.create(titulo='Estudiar', descripcion='Estudiar para el examen', usuario=usuario)
    
    assert tarea.titulo == 'Estudiar'
    assert tarea.descripcion == 'Estudiar para el examen'
    assert tarea.usuario == usuario  # Verificar que la tarea está asociada al usuario creado
