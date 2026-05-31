from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    es_instructor = models.BooleanField(default=False)
    bio = models.TextField(blank=True, default='')
    foto_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def get_iniciales(self):
        if self.first_name and self.last_name:
            return f'{self.first_name[0]}{self.last_name[0]}'.upper()
        return self.username[:2].upper()

    def total_cursos(self):
        from cursos.models import Inscripcion
        return Inscripcion.objects.filter(usuario=self).count()

    def __str__(self):
        return self.username
