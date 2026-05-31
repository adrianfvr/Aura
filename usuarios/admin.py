from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'es_instructor', 'total_cursos', 'is_staff', 'date_joined')
    list_filter = ('es_instructor', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_editable = ('es_instructor',)

    fieldsets = UserAdmin.fieldsets + (
        ('Perfil AURA', {
            'fields': ('es_instructor', 'bio', 'foto_perfil'),
        }),
    )
