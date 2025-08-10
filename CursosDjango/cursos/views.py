from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Actividad
from .forms import CursosForm, ActividadesForm
from django.db.models import ObjectDoesNotExist

# Create your views here.

# Funcionalidad de crud cursos.
def registrarCurso(request):
    if request.method == 'POST':
        form = CursosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cursos=Curso.objects.all()
            return render(request, "cursos/listaCursos.html", {'cursos': cursos})
        else:
            print(form.errors)
    form = CursosForm()
    return render(request, 'cursos/formCursos.html', {'form':form})

def listaCursos(request):
    cursos = Curso.objects.all()
    return render(request, "cursos/listaCursos.html", {'cursos': cursos})

def consultarCursoIndividual(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, "cursos/formEditarCurso.html", {'curso': curso})

def editarCurso(request, id):
    # 1. Obtener el objeto del curso
    # get_object_or_404 manejará el caso donde el curso no existe y devolverá un 404
    curso = get_object_or_404(Curso, pk=id)

    # 2. Manejar la solicitud POST (cuando el formulario se envía)
    if request.method == 'POST':
        try:
            # Actualizar los datos del curso con la información del formulario
            curso.titulo = request.POST.get('titulo')
            curso.descripcion = request.POST.get('descripcion')
            curso.precio = request.POST.get('precio')
            curso.nivel = request.POST.get('nivel')
            
            # El checkbox de disponibilidad se maneja de forma especial
            # Si el checkbox está marcado, 'disponibilidad' estará en request.POST
            # Si no está marcado, no estará.
            curso.disponibilidad = 'disponibilidad' in request.POST
            
            # Manejar la imagen
            # Si se carga una nueva imagen, request.FILES contendrá el archivo
            if 'imagen' in request.FILES:
                curso.imagen = request.FILES['imagen']

            # Guardar los cambios en la base de datos
            curso.save()
            
            # 5. Redireccionar a la lista de cursos o a una página de éxito
            return redirect('lista_cursos') # Asegúrate de que 'lista_cursos' es el nombre de tu URL
            
        except Exception as e:
            # Manejar errores si algo sale mal
            # Puedes agregar un mensaje de error o simplemente renderizar el formulario de nuevo
            return render(request, 'cursos/formEditarCurso.html', {'curso': curso, 'error': str(e)})

    # 3. Manejar la solicitud GET (cuando se accede a la página de edición)
    else:
        # Renderizar el formulario con los datos actuales del curso
        return render(request, 'cursos/formEditarCurso.html', {'curso': curso})
    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        form = CursosForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursosForm(instance=curso)

    return render(request, "cursos/formEditarCurso.html", {'form': form})

def eliminarCurso(request, id, confirmacion='cursos/confirmarEliminacionCurso.html'):
    curso = get_object_or_404(Curso, id=id)
    if request.method=='POST':
        curso.delete()
        cursos=Curso.objects.all()
        return render(request, "cursos/listaCursos.html", {'cursos':cursos})
    return render(request, confirmacion, {'object': curso})

# Funcionalidad de actividades.

def registrarActividad(request):
    if request.method == 'POST':
        form = ActividadesForm(request.POST)
        if form.is_valid():
            form.save()
            actividades=Actividad.objects.all()
            return render(request, "cursos/listaCursos.html", {'actividades': actividades})
        else:
            print(form.errors)
    form = ActividadesForm()
    return render(request, 'cursos/formCursos.html', {'form':form})

def listaActividades(request):
    actividades = Actividad.objects.all()
    return render(request, "cursos/listaActividades.html", {'actividades':actividades})

def eliminarActividad(request, id, confirmacion='cursos/confirmarEliminacionActividad.html'):
    actividad = get_object_or_404(Actividad, id=id)
    if request.method=='POST':
        actividad.delete()
        actividades=Actividad.objects.all()
        return render(request, "cursos/Actividades.html", {'actividades':actividades})
    return render(request, confirmacion, {'object': actividad})
