from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cursos.views import lista_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_cursos),
    path('', include('usuarios.urls')),
    path('', include('cursos.urls')),
    path('', include('dashboard.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)