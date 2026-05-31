from django.contrib import admin
from .models import Curso, Inscripcion


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instructor', 'total_inscritos', 'publicado', 'fecha_creacion')
    list_filter = ('publicado', 'fecha_creacion')
    search_fields = ('titulo', 'instructor__username')
    list_editable = ('publicado',)


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso', 'progreso', 'completado', 'fecha')
    list_filter = ('completado',)
    search_fields = ('usuario__username', 'curso__titulo')
