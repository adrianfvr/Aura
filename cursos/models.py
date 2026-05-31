from django.db import models
from usuarios.models import Usuario


class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    instructor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cursos_creados')
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo

    def total_inscritos(self):
        return self.inscripcion_set.count()


class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripcion_set')
    fecha = models.DateTimeField(auto_now_add=True)
    progreso = models.PositiveIntegerField(default=0)
    completado = models.BooleanField(default=False)
    ultima_actividad = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('usuario', 'curso')
        ordering = ['-ultima_actividad']

    def __str__(self):
        return f'{self.usuario.username} → {self.curso.titulo}'

    def marcar_progreso(self, valor):
        self.progreso = min(max(int(valor), 0), 100)
        self.completado = self.progreso >= 100
        self.save()
