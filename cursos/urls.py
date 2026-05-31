from django.urls import path
from .views import inscribirse, desinscribirse, crear_curso, editar_curso, detalle_curso, actualizar_progreso

urlpatterns = [
    path('inscribirse/<int:curso_id>/', inscribirse, name='inscribirse'),
    path('desinscribirse/<int:curso_id>/', desinscribirse, name='desinscribirse'),
    path('crear-curso/', crear_curso, name='crear_curso'),
    path('curso/<int:curso_id>/', detalle_curso, name='detalle_curso'),
    path('curso/<int:curso_id>/editar/', editar_curso, name='editar_curso'),
    path('curso/<int:curso_id>/progreso/', actualizar_progreso, name='actualizar_progreso'),
]
