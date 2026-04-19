from django.urls import path
from .views import inscribirse, crear_curso, detalle_curso

urlpatterns = [
    path('inscribirse/<int:curso_id>/', inscribirse, name='inscribirse'),
    path('crear-curso/', crear_curso, name='crear_curso'),
    path('curso/<int:curso_id>/', detalle_curso, name='detalle_curso'),
]