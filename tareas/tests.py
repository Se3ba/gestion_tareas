import pytest
from .models import Usuario, Tarea, Categoria

@pytest.mark.django_db
def test_usuario_creacion():
    usuario = Usuario.objects.create(nombre='Juan', email='juan@example.com')
    assert usuario.nombre == 'Juan'

@pytest.mark.django_db
def test_crear_tarea():
    usuario = Usuario.objects.create(nombre='Ana', email='ana@example.com')
    tarea = Tarea.objects.create(titulo='Estudiar', descripcion='Estudiar Django', usuario=usuario)
    assert tarea.titulo == 'Estudiar'
