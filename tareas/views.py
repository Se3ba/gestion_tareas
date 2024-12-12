from django.shortcuts import render, get_object_or_404
from .models import Usuario, Tarea, Categoria
from django.http import JsonResponse

def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        usuario = Usuario.objects.create(nombre=nombre, email=email)
        return JsonResponse({'message': 'Usuario registrado', 'usuario_id': usuario.id})
    return render(request, 'registrar_usuario.html')

def crear_tarea(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        usuario_id = request.POST['usuario_id']
        categorias_ids = request.POST.getlist('categorias')
        usuario = get_object_or_404(Usuario, id=usuario_id)
        tarea = Tarea.objects.create(titulo=titulo, descripcion=descripcion, usuario=usuario)
        tarea.categorias.set(categorias_ids)
        return JsonResponse({'message': 'Tarea creada', 'tarea_id': tarea.id})
    return render(request, 'crear_tarea.html')

def tareas_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    tareas = Tarea.objects.filter(categorias=categoria)
    return render(request, 'tareas_por_categoria.html', {'categoria': categoria, 'tareas': tareas})
