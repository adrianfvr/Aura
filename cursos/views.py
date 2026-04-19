from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso, Inscripcion
from .forms import CursoForm

def es_instructor(user):
    return user.es_instructor

@login_required
def lista_cursos(request):
    query = request.GET.get('q')
    cursos = Curso.objects.all()

    if query:
        cursos = cursos.filter(titulo__icontains=query)

    return render(request, 'cursos.html', {'cursos': cursos})
  
@login_required
def inscribirse(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    # Evitar duplicados
    existe = Inscripcion.objects.filter(usuario=request.user, curso=curso).exists()

    if not existe:
        Inscripcion.objects.create(usuario=request.user, curso=curso)

    return redirect('/')
  

@login_required
@user_passes_test(es_instructor,login_url='/')
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.instructor = request.user
            curso.save()
            return redirect('/')
    else:
        form = CursoForm()

    return render(request, 'crear_curso.html', {'form': form})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    inscrito = False
    if request.user.is_authenticated:
        inscrito = Inscripcion.objects.filter(
            usuario=request.user,
            curso=curso
        ).exists()

    return render(request, 'detalle_curso.html', {
        'curso': curso,
        'inscrito': inscrito
    })