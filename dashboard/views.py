from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cursos.models import Inscripcion

@login_required
def dashboard(request):
    inscripciones = Inscripcion.objects.filter(usuario=request.user)
    return render(request, 'dashboard.html', {'inscripciones': inscripciones})