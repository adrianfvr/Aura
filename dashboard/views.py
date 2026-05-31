from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cursos.models import Inscripcion, Curso


@login_required
def dashboard(request):
    inscripciones = Inscripcion.objects.filter(
        usuario=request.user
    ).select_related('curso', 'curso__instructor')

    completados = inscripciones.filter(completado=True).count()
    en_progreso = inscripciones.filter(completado=False, progreso__gt=0).count()
    sin_iniciar = inscripciones.filter(progreso=0).count()

    # promedio general
    total = inscripciones.count()
    if total > 0:
        suma = sum(i.progreso for i in inscripciones)
        promedio = round(suma / total)
    else:
        promedio = 0

    # es instructor
    mis_cursos_creados = []
    if request.user.es_instructor:
        mis_cursos_creados = Curso.objects.filter(
            instructor=request.user
        ).order_by('-fecha_creacion')

    return render(request, 'dashboard.html', {
        'inscripciones': inscripciones,
        'completados': completados,
        'en_progreso': en_progreso,
        'sin_iniciar': sin_iniciar,
        'promedio': promedio,
        'total': total,
        'mis_cursos_creados': mis_cursos_creados,
    })
