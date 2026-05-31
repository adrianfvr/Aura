from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Curso, Inscripcion
from .forms import CursoForm


def es_instructor(user):
    return user.es_instructor


def lista_cursos(request):
    query = request.GET.get('q', '').strip()
    cursos = Curso.objects.filter(publicado=True)
    if query:
        cursos = cursos.filter(titulo__icontains=query)
    return render(request, 'cursos.html', {
        'cursos': cursos,
        'query': query,
        'total': cursos.count(),
    })


@login_required
def inscribirse(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id, publicado=True)
    existe = Inscripcion.objects.filter(usuario=request.user, curso=curso).exists()
    if not existe:
        Inscripcion.objects.create(usuario=request.user, curso=curso)
        messages.success(request, f'¡Te inscribiste en "{curso.titulo}"!')
    else:
        messages.info(request, f'Ya estás inscrito en "{curso.titulo}".')
    return redirect('detalle_curso', curso_id=curso_id)


@login_required
def desinscribirse(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    eliminado = Inscripcion.objects.filter(usuario=request.user, curso=curso).delete()
    if eliminado[0]:
        messages.success(request, f'Te desinscribiste de "{curso.titulo}".')
    return redirect('detalle_curso', curso_id=curso_id)


@login_required
@user_passes_test(es_instructor, login_url='/')
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.instructor = request.user
            curso.save()
            messages.success(request, f'Curso "{curso.titulo}" publicado con éxito')
            return redirect('detalle_curso', curso_id=curso.id)
        else:
            messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = CursoForm()
    return render(request, 'crear_curso.html', {'form': form})


@login_required
@user_passes_test(es_instructor, login_url='/')
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id, instructor=request.user)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, f'Curso "{curso.titulo}" actualizado.')
            return redirect('detalle_curso', curso_id=curso.id)
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'crear_curso.html', {'form': form, 'editando': True, 'curso': curso})


@login_required
def actualizar_progreso(request, curso_id):
    if request.method == 'POST':
        inscripcion = get_object_or_404(Inscripcion, usuario=request.user, curso_id=curso_id)
        valor = request.POST.get('progreso', 0)
        inscripcion.marcar_progreso(valor)
        messages.success(request, 'Progreso actualizado.')
    return redirect('detalle_curso', curso_id=curso_id)


def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    inscrito = False
    inscripcion = None
    if request.user.is_authenticated:
        try:
            inscripcion = Inscripcion.objects.get(usuario=request.user, curso=curso)
            inscrito = True
        except Inscripcion.DoesNotExist:
            pass
    return render(request, 'detalle_curso.html', {
        'curso': curso,
        'inscrito': inscrito,
        'inscripcion': inscripcion,
    })


def pagina_404(request, exception):
    return render(request, '404.html', status=404)
